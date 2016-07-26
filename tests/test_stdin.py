"""Run the demo."""

from click.testing import CliRunner
from proselint.command_line import proselint, demo_file

runner = CliRunner()
demo = runner.invoke(proselint, ['--demo'])
assert demo.exit_code == 1

with open(demo_file) as f:
    stdin = runner.invoke(proselint, ['--stdin'], input=f.read())

assert stdin.exit_code == 1
    
assert stdin.output == demo.output.replace(demo_file, 'stdin')


