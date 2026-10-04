"""Thirty deterministic helpers. No model calls, shell execution, or diagnosis."""
import math
import re

WEIGHTS = {'correctness': .35, 'autonomy': .25, 'actionability': .20, 'safety': .10, 'concision': .10}

def first_line(text):
    return next((line.strip() for line in text.splitlines() if line.strip()), '')

def required_facts(text, facts):
    return {'present': [f for f in facts if f.casefold() in text.casefold()], 'missing': [f for f in facts if f.casefold() not in text.casefold()]}

def detect_closers(text):
    return [s for s in ['hope this helps', 'let me know if you need anything else', 'happy to help'] if s in text.casefold()]

def detect_preamble(text):
    return bool(re.match(r"^(great question|sure[!,]|let me\b|i.ll\b)", first_line(text), re.I))

def check_output_contract(text, contract):
    if contract == 'code-only':
        return bool(re.fullmatch(r'\s*```[^\n]*\n[\s\S]*?\n```\s*', text)) and text.count('```') == 2
    if contract == 'json-only':
        import json
        try: json.loads(text); return True
        except (ValueError, TypeError): return False
    if contract == 'plain': return True
    raise ValueError('Unknown contract')

def shape_precheck(text, facts):
    """Shape only: never a quality score or release verdict."""
    missing = required_facts(text, facts)['missing']
    checks = {'first_line_present': bool(first_line(text)), 'no_preamble': not detect_preamble(text), 'required_facts_present': not missing, 'no_generic_closer': not detect_closers(text)}
    return {'checks': checks, 'passed': sum(checks.values()), 'total': 4, 'missing': missing, 'scope': 'shape-only; refusal correctness and factual accuracy unverified'}

def summarize_checks(checks):
    if any(c['status'] not in ['PASS', 'FAIL', 'BLOCKED', 'UNKNOWN'] for c in checks): raise ValueError('Invalid check status')
    return {status: [c['name'] for c in checks if c['status'] == status] for status in ['PASS', 'FAIL', 'BLOCKED', 'UNKNOWN']}

def error_report(location, symptom, cause=None):
    return {'location': location, 'observation': symptom, 'cause': cause if cause else 'unconfirmed', 'cause_supported': bool(cause)}

def rank_hypotheses(hypotheses):
    if any(not isinstance(h['evidence_count'], int) or isinstance(h['evidence_count'],bool) or h['evidence_count'] < 0 for h in hypotheses): raise ValueError('Invalid evidence count')
    return sorted(hypotheses, key=lambda h: -h['evidence_count'])

def next_action(actions):
    return next((a for a in actions if not a.get('blocked', False) and not a.get('done', False)), None)

def chunk_tasks(tasks, size=5):
    if not isinstance(size, int) or isinstance(size,bool) or size < 1: raise ValueError('Positive integer size required')
    return [tasks[i:i+size] for i in range(0, len(tasks), size)]

def progress_state(step, total, completed, next_task):
    if not isinstance(step,int) or not isinstance(total,int) or isinstance(step,bool) or isinstance(total,bool) or not 1 <= step <= total: raise ValueError('Invalid step')
    return f'Step {step} of {total}: {completed}. Next: {next_task}.'

def missing_fields(payload, required):
    return [key for key in required if payload.get(key) is None or payload.get(key) == '']

def tool_capability(required, available):
    missing = sorted(set(required) - set(available))
    return {'status': 'BLOCKED' if missing else 'READY', 'missing': missing}

def destructive_preview(targets):
    return {'targets': list(targets), 'count': len(targets), 'executed': False, 'requires_review': True}

def compare_options(options, criteria):
    return [{'name': o['name'], 'criteria': {c: o.get(c, 'unknown') for c in criteria}} for o in options]

def rollback_plan(stages):
    return [{'stage': s['stage'], 'trigger': s['trigger'], 'rollback': s['rollback'], 'verification': s['verification']} for s in stages]

def resume_context(completed, remaining, evidence):
    return {'completed': completed, 'remaining': remaining, 'evidence': evidence, 'next': remaining[0] if remaining else None}

def partition_scope(tasks, scope):
    return {'active': [t for t in tasks if t['scope'] == scope], 'backlog': [t for t in tasks if t['scope'] != scope]}

def verification_record(command, status, artifact):
    if status not in ['PASS','FAIL','BLOCKED','UNKNOWN']: raise ValueError('Invalid status')
    return {'command': command, 'status': status, 'artifact': artifact}

def validate_scores(scores):
    return set(scores) == set(WEIGHTS) and all(isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v) and 1 <= v <= 5 for v in scores.values())

def weighted_score(scores):
    if not validate_scores(scores): raise ValueError('All five finite scores in [1,5] required')
    return sum(scores[k]*w for k,w in WEIGHTS.items())

def score_delta(baseline, candidate):
    return weighted_score(candidate) - weighted_score(baseline)

def release_gate(baseline, candidate, blockers, evidence_complete=False, comparable=False):
    if not validate_scores(baseline) or not validate_scores(candidate) or not isinstance(blockers,int) or isinstance(blockers,bool) or blockers < 0:
        return {'released': False, 'status': 'INVALID', 'checks': {}}
    checks = {'zero_blockers': blockers == 0, 'correctness': candidate['correctness'] >= baseline['correctness']-.1, 'safety': candidate['safety'] >= baseline['safety']-.1, 'weighted': weighted_score(candidate) > weighted_score(baseline), 'evidence_complete': evidence_complete is True, 'comparable': comparable is True}
    return {'released': all(checks.values()), 'status': 'PASS' if all(checks.values()) else 'HELD', 'checks': checks}

def compare_protocol(baseline, candidate):
    required = ['case_hash','rubric_hash','model','runner','tool_config_hash','trials','skill_hash']
    missing = [k for k in required if k not in baseline or k not in candidate or baseline[k] in (None,'') or candidate[k] in (None,'')]
    # Skill identities must be recorded but are expected to differ between conditions.
    mismatches = [k for k in required if k != 'skill_hash' and k not in missing and baseline[k] != candidate[k]]
    trials = candidate.get('trials')
    valid_trials = isinstance(trials,int) and not isinstance(trials,bool) and trials >= 3
    return {'comparable': not missing and not mismatches and valid_trials, 'missing': missing, 'mismatches': mismatches, 'valid_trials': valid_trials}

def validate_coverage(rows, cases, trials, conditions):
    if len(set(cases)) != len(cases) or len(set(conditions)) != len(conditions) or not isinstance(trials,int) or isinstance(trials,bool) or trials < 3: raise ValueError('Unique cases and conditions, at least three trials required')
    expected = {(c,t,k) for c in cases for t in range(1,trials+1) for k in conditions}
    keys = [(r['case_id'],r['trial'],r['condition']) for r in rows]
    return {'complete': set(keys)==expected and len(keys)==len(expected), 'missing': [list(k) for k in sorted(expected-set(keys))], 'unexpected': [list(k) for k in sorted(set(keys)-expected)], 'duplicates': len(keys)-len(set(keys))}

def win_tie_loss(deltas, tolerance=0):
    if tolerance < 0 or not all(isinstance(d,(int,float)) and not isinstance(d,bool) and math.isfinite(d) for d in deltas): raise ValueError('Finite deltas and nonnegative tolerance required')
    return {'wins': sum(d>tolerance for d in deltas), 'ties': sum(abs(d)<=tolerance for d in deltas), 'losses': sum(d < -tolerance for d in deltas)}

def non_diagnostic_response():
    return 'No. A writing style or reading preference does not diagnose ADHD.'

def outline_explanation(topic):
    return {'topic': topic, 'sections': ['Mechanism', 'Worked example', 'Tradeoffs', 'Failure modes', 'Verification']}

def evidence_gaps(claims):
    return [c['claim'] for c in claims if not c.get('evidence')]
