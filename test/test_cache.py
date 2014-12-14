# encoding: utf-8

#import pytest

from unittest import TestCase

from marrow.package.cache import PluginCache

#from test import helper

from pytest import main as pytest
from coverage import main as coverage
from tox import cmdline as tox
from virtualenv import main as virtualenv


class TestPluginCache(TestCase):
	candidates = ('py.test', 'coverage', 'tox', 'virtualenv')
	
	def test__cache__loads_expected_objects(self):
		cache = PluginCache('console_scripts')
		for candidate, obj in zip(self.candidates, (pytest, coverage, tox, virtualenv)):
			assert cache[candidate] is obj
	
	def test__cache__attribute_access(self):
		cache = PluginCache('console_scripts')
		assert cache.coverage is coverage
	
	def test__cache__actually_caches_things(self):
		cache = PluginCache('console_scripts')
		assert len(cache) == 0
		assert 'coverage' not in cache
		assert cache.coverage is coverage
		assert len(cache) == 1
		assert 'coverage' in cache
