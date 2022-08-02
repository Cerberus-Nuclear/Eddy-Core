
""" To run: just call python -m pytest while in this directory
or add a configuration in pycharm
"""

import pytest
from eddymc_core import eddy
from tests import mcnp_examples, scale_examples
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources


@pytest.fixture
def f2_file(tmpdir):
    f2 = pkg_resources.read_text(mcnp_examples, 'F2.out')
    return f2.split('\n')


@pytest.fixture
def mcnp4c_file(tmpdir):
    mcnp4c = pkg_resources.read_text(mcnp_examples, 'mcnp4c.out')
    return mcnp4c.split('\n')


@pytest.fixture
def scale_file(tmpdir):
    file = pkg_resources.read_text(scale_examples, 'cylinder_ce.out')
    return file.split('\n')


@pytest.fixture
def text_file(tmpdir):
    file = pkg_resources.read_text(mcnp_examples, 'not_an_mcnp_file.out')
    return file.split('\n')


@pytest.fixture
def crit_file(tmpdir):
    file = pkg_resources.read_text(mcnp_examples, 'Criticality.out')
    return file.split('\n')


@pytest.fixture
def mcnp_input(tmpdir):
    file = pkg_resources.read_text(mcnp_examples, 'F4.mcnp')
    return file.split('\n')


def test_crit_checker_positive(crit_file):
    # arrange
    text = crit_file
    # act
    result = eddy.check_if_crit(text)
    # assert
    assert result is True


def test_crit_checker_negative(f2_file):
    # arrange
    text = f2_file
    # act
    result = eddy.check_if_crit(text)
    # assert
    assert result is False


def test_read_file():
    # arrange
    file = "mcnp_examples/F2.out"
    # act
    data = eddy.read_file(file)
    # assert
    assert data[0].strip() == "Code Name &amp; Version = MCNP_6.20, 6.2.0"
    assert len(data) == 884


def test_sanitize_list():
    # arrange
    test_text = [
        "This is ordinary text",
        "This has a <h1> </h1> symbol in it",
        "This has a \" symbol in it",
        "This has a & in it.",
        ]
    # act
    sanitized_text = eddy.sanitize_list(test_text)
    # assert
    assert sanitized_text[0] == "This is ordinary text"
    assert sanitized_text[1] == "This has a &lt;h1&gt; &lt;/h1&gt; symbol in it"
    assert sanitized_text[2] == "This has a &#34; symbol in it"
    assert sanitized_text[3] == "This has a &amp; in it."


def test_get_args_with_passed_arguments():
    # arrange
    name = 'mcnp_examples/F2.out'
    # act
    output_data, code, crit = eddy.get_args(name)
    # assert
    assert name == 'mcnp_examples/F2.out'
    assert code == 'MCNP'
    assert crit is False


def test_recognizes_SCALE():
    # arrange
    scale_file = 'scale_examples/cylinder_ce.out'
    # act
    output, code, crit = eddy.get_args(scale_file)
    # assert
    assert code == 'SCALE'


def test_recognizes_MCNP():
    # arrange
    mcnp_file = 'mcnp_examples/F4.out'
    # act
    output, code, crit = eddy.get_args(mcnp_file)
    # assert
    assert code == 'MCNP'


def test_recognizes_non_mcnp_input(mocker):
    # arrange
    file = 'mcnp_examples/not_an_mcnp_file.out'
    mocked_eddy_scale_case = mocker.patch('eddymc_core.scale.eddy_scale_case.EddySCALECase.__init__')
    mocked_eddy_mcnp_case = mocker.patch('eddymc_core.mcnp.eddy_mcnp_case.EddyMCNPCase.__init__.__init__')
    # act
    with pytest.raises(eddy.NotAcceptedFileTypeError) as expected_failure:
        eddy.get_args(file)
    # assert
    assert expected_failure
    mocked_eddy_mcnp_case.assert_not_called()
    mocked_eddy_scale_case.assert_not_called()


def test_main_calls_eddy_scale_case(mocker, scale_file):
    # arrange
    name = 'scale_examples/cylinder_ce.out'
    data = scale_file
    sf = 3.141592
    crit = False
    code = 'SCALE'
    mocker.patch('eddymc_core.eddy.get_args', return_value=(data, code, crit,))
    mocked_eddy_mcnp_case = mocker.patch('eddymc_core.mcnp.eddy_mcnp_case.EddyMCNPCase.__init__')
    mocked_eddy_scale_case = mocker.patch('eddymc_core.scale.eddy_scale_case.EddySCALECase.__init__', return_value=None)
    mocker.patch('eddymc_core.scale.scale_html_writer.get_html', return_value='test_html')
    mocker.patch('eddymc_core.eddy.write_output')
    # act
    eddy.main(filename=name, scaling_factor=sf)
    # assert
    mocked_eddy_mcnp_case.assert_not_called()
    mocked_eddy_scale_case.assert_called()


def test_main_calls_eddy_mcnp_case(mocker, f2_file):
    # arrange
    name = 'mcnp_examples/F2.out'
    data = f2_file
    sf = 3.141592
    crit = False
    code = 'MCNP'
    mocker.patch('eddymc_core.eddy.get_args', return_value=(data, code, crit,))
    mocked_eddy_scale_case = mocker.patch('eddymc_core.scale.eddy_scale_case.EddySCALECase.__init__')
    mocked_eddy_mcnp_case = mocker.patch('eddymc_core.mcnp.eddy_mcnp_case.EddyMCNPCase.__init__', return_value=None)
    mocker.patch('eddymc_core.mcnp.mcnp_html_writer.get_html', return_value='test_html')
    mocker.patch('eddymc_core.eddy.write_output')
    # act
    eddy.main(filename=name, scaling_factor=sf)
    # assert
    mocked_eddy_mcnp_case.assert_called()
    mocked_eddy_scale_case.assert_not_called()


def test_main_calls_eddy_mcnp_case_for_mcnp4c(mocker, mcnp4c_file):
    # arrange
    name = 'mcnp_examples/mcnp4c.out'
    data = mcnp4c_file
    data = eddy.sanitize_list(data)  # not ideal re-using this in test
    sf = 3.141592
    crit = False
    code = 'MCNP'
    mocker.patch('eddymc_core.eddy.get_args', return_value=(data, code, crit,))
    mocked_eddy_scale_case = mocker.patch('eddymc_core.scale.eddy_scale_case.EddySCALECase.__init__')
    mocked_eddy_mcnp_case = mocker.patch('eddymc_core.mcnp.eddy_mcnp_case.EddyMCNPCase.__init__', return_value=None)
    mocker.patch('eddymc_core.mcnp.mcnp_html_writer.get_html', return_value='test_html')
    mocker.patch('eddymc_core.eddy.write_output')
    # act
    eddy.main(filename=name, scaling_factor=sf)
    # assert
    mocked_eddy_mcnp_case.assert_called()
    mocked_eddy_scale_case.assert_not_called()


def test_main_calls_html_writer(mocker, f2_file):
    # arrange
    name = 'mcnp_examples/F2.out'
    sf = 1234
    data = f2_file
    crit = False
    code = 'MCNP'
    mocker.patch('eddymc_core.eddy.get_args', return_value=(data, code, crit,))
    mocked_html_writer = mocker.patch('eddymc_core.mcnp.mcnp_html_writer.get_html', return_value=None)
    mocker.patch('eddymc_core.mcnp.eddy_mcnp_case.EddyMCNPCase.__init__', return_value=None)
    mocker.patch('eddymc_core.eddy.write_output')
    # act
    eddy.main(filename=name, scaling_factor=sf)
    # assert
    mocked_html_writer.assert_called()


def test_main_with_non_mc_input(mocker):
    # arrange
    name = 'mcnp_examples/not_an_mcnp_file.out'
    sf = 1.2
    mocked_eddy_scale_case = mocker.patch('eddymc_core.scale.eddy_scale_case.EddySCALECase.__init__')
    mocked_eddy_mcnp_case = mocker.patch('eddymc_core.mcnp.eddy_mcnp_case.EddyMCNPCase.__init__.__init__')
    # act
    with pytest.raises(eddy.NotAcceptedFileTypeError) as expected_failure:
        eddy.main(name, sf)
    # assert
    mocked_eddy_mcnp_case.assert_not_called()
    mocked_eddy_scale_case.assert_not_called()
    assert expected_failure


def test_main_with_nonexistent_input_passed():
    # arrange
    name = 'mcnp_examples/nonexistent_file.out'
    # act
    # actually fails in get_filename()
    with pytest.raises(AssertionError) as expected_failure:
        eddy.main(name)
    # assert
    assert expected_failure
