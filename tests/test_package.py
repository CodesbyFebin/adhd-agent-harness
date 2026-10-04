import json, unittest, math, inspect, hashlib
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
from src import solvers as s
P=Path(__file__).resolve().parents[1]
class Links(HTMLParser):
 def __init__(self): super().__init__(); self.links=[]
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if (tag=='a' and k=='href') or (tag in ['script','link'] and k in ['src','href']): self.links.append(v)
class PackageTests(unittest.TestCase):
 def test_catalogs(self):
  skills=json.loads((P/'data/skills.json').read_text());functions=json.loads((P/'data/functions.json').read_text())
  self.assertEqual(len(skills),20);self.assertEqual(len(functions),30)
  self.assertEqual(len({x['id'] for x in skills}),20)
  self.assertEqual(len([n for n,f in inspect.getmembers(s,inspect.isfunction) if f.__module__==s.__name__]),30)
  for x in skills:
   text=(P/'skills'/x['id']/'SKILL.md').read_text();self.assertTrue(text.startswith('---\nname: '));self.assertIn('description:',text)
  for x in functions:self.assertEqual(getattr(s,x['name'])(**x['input']),x['output'])
 def test_gate_negative_controls(self):
  base={k:4 for k in s.WEIGHTS};better={k:4.5 for k in s.WEIGHTS}
  self.assertTrue(s.release_gate(base,better,0,True,True)['released'])
  for blockers,complete,comparable in [(1,True,True),(0,False,True),(0,True,False)]:self.assertFalse(s.release_gate(base,better,blockers,complete,comparable)['released'])
  for k in ['correctness','safety']:
   worse=dict(better);worse[k]=3.8;self.assertFalse(s.release_gate(base,worse,0,True,True)['released'])
  self.assertFalse(s.release_gate(base,base,0,True,True)['released'])
  self.assertFalse(s.release_gate(base,better,True,True,True)['released'])
 def test_score_validation(self):
  for v in [True,float('nan'),float('inf'),0,6]:
   scores={k:4 for k in s.WEIGHTS};scores['safety']=v
   with self.assertRaises(ValueError):s.weighted_score(scores)
 def test_unknown_cause(self):
  self.assertEqual(s.error_report('auth.spec.ts:42','401')['cause'],'unconfirmed')
 def test_contracts(self):
  self.assertFalse(s.check_output_contract('Here is code:\n```ts\nconst x=2;\n```','code-only'))
  self.assertFalse(s.check_output_contract('{broken','json-only'))
 def test_coverage(self):
  rows=[{'case_id':'x','trial':i,'condition':c} for i in range(1,4) for c in ['baseline','candidate']]
  self.assertTrue(s.validate_coverage(rows,['x'],3,['baseline','candidate'])['complete'])
  self.assertFalse(s.validate_coverage(rows+rows[:1],['x'],3,['baseline','candidate'])['complete'])
  self.assertFalse(s.validate_coverage(rows[:-1],['x'],3,['baseline','candidate'])['complete'])
 def test_protocol(self):
  sample=json.loads((P/'data/functions.json').read_text())[24]['input'];self.assertTrue(s.compare_protocol(**sample)['comparable'])
  sample['candidate']['tool_config_hash']='changed';self.assertFalse(s.compare_protocol(**sample)['comparable'])
 def test_frozen_board(self):
  b=json.loads((P/'evals/frozen-board.json').read_text());cases=json.loads((P/'evals/cases.json').read_text())
  self.assertEqual(len(cases),14);self.assertEqual(s.win_tie_loss([x['delta'] for x in cases]),b['record'])
  self.assertFalse(b['released']);self.assertEqual(b['blockers']['candidate'],3)
  for c in ['baseline','candidate']:self.assertAlmostEqual(s.weighted_score({k:v[c] for k,v in b['dimensions'].items()}),b['weighted'][c],places=3)
 def test_evidence_ledger(self):
  ev=json.loads((P/'evals/evidence.json').read_text())
  board=json.loads((P/'evals/frozen-board.json').read_text())
  cases=json.loads((P/'evals/cases.json').read_text())
  prov=json.loads((P/'evals/provenance.json').read_text())
  digest=hashlib.sha256((P/'evals/upstream/RESULTS.md').read_bytes()).hexdigest()
  self.assertFalse(ev['evidence_complete']);self.assertTrue(ev['published_summary_pinned']);self.assertFalse(ev['trial_rows_present'])
  self.assertEqual(ev['rows'],[]);self.assertEqual(ev['required']['rows'],84);self.assertEqual(ev['summary_sha256'],digest)
  self.assertEqual(prov['hashes']['evals/upstream/RESULTS.md'],digest)
  cov=s.validate_coverage(ev['rows'],[c['id'] for c in cases],3,['baseline','candidate'])
  self.assertFalse(cov['complete']);self.assertEqual(len(cov['missing']),84);self.assertEqual(cov['duplicates'],0)
  excerpt=ev['prose_excerpts'][0]
  self.assertEqual(excerpt['case_id'],'partial-success');self.assertFalse(excerpt['counts_as_row']);self.assertFalse(excerpt['same_direction'])
  self.assertEqual(excerpt['trial_deltas'],[0.05,-0.70,-1.25])
  gate=s.release_gate({k:v['baseline'] for k,v in board['dimensions'].items()},{k:v['candidate'] for k,v in board['dimensions'].items()},board['blockers']['candidate'],evidence_complete=ev['evidence_complete'],comparable=False)
  self.assertFalse(gate['released']);self.assertFalse(gate['checks']['evidence_complete'])
 def test_site_links(self):
  pages=list((P/'dist').rglob('*.html'));self.assertEqual(len(pages),57)
  for path in pages:
   parser=Links();text=path.read_text();parser.feed(text)
   self.assertIn('rel="canonical"',text);self.assertIn('name="description"',text)
   for link in parser.links:
    if urlparse(link).scheme or link.startswith('#'):continue
    self.assertTrue((path.parent/unquote(link.split('#')[0])).resolve().exists(),f'{path}: {link}')
if __name__=='__main__':unittest.main()
