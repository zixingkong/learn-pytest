# Pytest学习文档一
## Pytest的用例发现
> pytest implements the following standard test discovery:

If no arguments are specified then collection starts from testpaths (if configured) or the current directory. Alternatively, command line arguments can be used in any combination of directories, file names or node ids.

Recurse into directories, unless they match norecursedirs.

In those directories, search for test_*.py or *_test.py files, imported by their test package name.

From those files, collect test items:

test prefixed test functions or methods outside of class

test prefixed test functions or methods inside Test prefixed test classes (without an __init__ method)

For examples of how to customize your test discovery Changing standard (Python) test discovery.

Within Python modules, pytest also discovers tests using the standard unittest.TestCase subclassing technique.
>

## pytest的fixtures
```shell
cache -- .../_pytest/cacheprovider.py:510
    Return a cache object that can persist state between testing sessions.

capsys -- .../_pytest/capture.py:878
    Enable text capturing of writes to ``sys.stdout`` and ``sys.stderr``.

capsysbinary -- .../_pytest/capture.py:895
    Enable bytes capturing of writes to ``sys.stdout`` and ``sys.stderr``.

capfd -- .../_pytest/capture.py:912
    Enable text capturing of writes to file descriptors ``1`` and ``2``.

capfdbinary -- .../_pytest/capture.py:929
    Enable bytes capturing of writes to file descriptors ``1`` and ``2``.

doctest_namespace [session scope] -- .../_pytest/doctest.py:731
    Fixture that returns a :py:class:`dict` that will be injected into the
    namespace of doctests.

pytestconfig [session scope] -- .../_pytest/fixtures.py:1334
    Session-scoped fixture that returns the session's :class:`pytest.Config`
    object.

record_property -- .../_pytest/junitxml.py:282
    Add extra properties to the calling test.

record_xml_attribute -- .../_pytest/junitxml.py:305
    Add extra xml attributes to the tag for the calling test.

record_testsuite_property [session scope] -- .../_pytest/junitxml.py:343
    Record a new ``<property>`` tag as child of the root ``<testsuite>``.

tmpdir_factory [session scope] -- .../_pytest/legacypath.py:295
    Return a :class:`pytest.TempdirFactory` instance for the test session.

tmpdir -- .../_pytest/legacypath.py:302
    Return a temporary directory path object which is unique to each test
    function invocation, created as a sub directory of the base temporary
    directory.

caplog -- .../_pytest/logging.py:487
    Access and control log capturing.

monkeypatch -- .../_pytest/monkeypatch.py:29
    A convenient fixture for monkey-patching.

recwarn -- .../_pytest/recwarn.py:29
    Return a :class:`WarningsRecorder` instance that records all warnings emitted by test functions.

tmp_path_factory [session scope] -- .../_pytest/tmpdir.py:184
    Return a :class:`pytest.TempPathFactory` instance for the test session.

tmp_path -- .../_pytest/tmpdir.py:199
    Return a temporary directory path object which is unique to each test
    function invocation, created as a sub directory of the base temporary
    directory.
```
## 其他用法
1. 常用功能
```shell
# Run tests by marker expressions
pytest -m slow

pytest --version   # shows where pytest was imported from
pytest --fixtures  # show available builtin function arguments
pytest -h | --help # show help on command line and config file options
#To get a list of the slowest 10 test durations over 1.0s long:
pytest --durations=10 --durations-min=1.0
```

2. 加载插件
```shell
#Managing loading of plugins
#Early loading plugins
pytest -p mypluginmodule
pytest -p pytest_cov
#Disabling plugins
pytest -p no:doctest
```

[comment]: <> (Calling pytest from Python code )
retcode = pytest.main()