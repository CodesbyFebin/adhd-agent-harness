import argparse, json, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src import solvers
a=argparse.ArgumentParser(description="Run a deterministic helper on JSON stdin")
a.add_argument("function")
args=a.parse_args()
catalog=json.loads((Path(__file__).resolve().parents[1]/"data/functions.json").read_text())
if args.function not in {f["name"] for f in catalog}: a.error("Unknown function")
try:
 print(json.dumps(getattr(solvers,args.function)(**json.load(sys.stdin)),indent=2))
except (ValueError,TypeError,KeyError) as exc:
 print(str(exc),file=sys.stderr); sys.exit(2)
