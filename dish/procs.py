from subprocess import Popen, PIPE
import sys
import time
import copy
from abc import ABC, abstractmethod
import click
from . import parser


class BaseProcess(ABC):
	@abstractmethod
	def __init__(self, args):
		pass

	@abstractmethod
	def run(self, stdin, stdout, stderr):
		pass

	@abstractmethod
	def send_signal(self, signal):
		pass

	@abstractmethod
	def communicate(self):
		pass


class RealProcess(BaseProcess):
	def __init__(self, args):
		self.args = args
		self._proc = None

	def run(self, stdin, stdout, stderr):
		self._proc = Popen(
			self.args, stdin=stdin, stdout=stdout, stderr=stderr,
		)
		#self.stdin = self._proc.stdin
		#self.stdout = self._proc.stdout
		#self.stderr = self._proc.stderr
		#self.stdin = stdin
		#self.stdout = stdout
		#self.stderr = stderr

	def send_signal(self, signal):
		self._proc.send_signal(signal)

	def communicate(self):
		self._proc.communicate()

	def __getattr__(self, name):
		return getattr(self._proc, name)


def run_pipeline(procs):
	# Run processes
	for i, proc in enumerate(procs):
		# Only process
		if len(procs) == 1:
			proc.run(stdin=None, stdout=None, stderr=None)
		# First process
		elif i == 0:
			proc.run(stdin=sys.stdin, stdout=PIPE, stderr=sys.stderr)
		# Last process
		elif i == len(procs) - 1:
			previous = procs[i-1]
			proc.run(stdin=previous.stdout, stdout=sys.stdout, stderr=sys.stderr)
		# Processes in the middle
		else:
			previous = procs[i-1]
			proc.run(stdin=previous.stdout, stdout=PIPE, stderr=sys.stderr)
		time.sleep(0.1)
	for proc in procs:
		proc.communicate()


def run_line(line, echo_args):
	args = parser.split_args(line)
	cmds = parser.split_pipeline(args)
	if echo_args:
		click.echo(repr([i for i in cmds]))
		# Recreate the cmds generator because the line above has caused it to
		# be used up
		cmds = parser.split_pipeline(args)
	procs = [RealProcess(i) for i in cmds]
	run_pipeline(procs)
