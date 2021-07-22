import pytest
from eddymc_core.scale.eddy_scale_case import EddySCALECase
from eddymc_core.scale import eddy_scale_case
from tests import scale_examples

try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources


class MockEddySCALECase(EddySCALECase):
    def __init__(self, filepath, scaling_factor, file):
        self.filepath = filepath
        self.name = filepath.replace('\\', '/').split('/')[-1]
        self.scaling_factor = scaling_factor
        self.file = file


@pytest.fixture
def ce_623_file(tmpdir):
    file = pkg_resources.read_text(scale_examples, 'cylinder_ce.out')
    return file.split('\n')


@pytest.fixture
def ce_624_file(tmpdir):
    file = pkg_resources.read_text(scale_examples, 'cylinder_ce_6_2_4.out')
    return file.split('\n')


@pytest.fixture
def multigroup_623_file(tmpdir):
    file = pkg_resources.read_text(scale_examples, 'cylinder_multigroup.out')
    return file.split('\n')


@pytest.fixture
def multigroup_624_file(tmpdir):
    file = pkg_resources.read_text(scale_examples, 'cylinder_multigroup_6_2_4.out')
    return file.split('\n')


@pytest.fixture
def simple_case(ce_623_file, tmpdir):
    return MockEddySCALECase(
        filepath="scale_examples/cylinder_ce.out",
        scaling_factor=1234,
        file=ce_623_file,
    )


@pytest.fixture
def multigroup_case(multigroup_623_file, tmpdir):
    return MockEddySCALECase(
        filepath="scale_examples/cylinder_multigroup.out",
        scaling_factor=1234,
        file=multigroup_623_file,
    )


@pytest.fixture
def mixing_table_ce_623(tmpdir):
    return [
        "                                        mixing table ",
        "",
        " mixture =     1          density(g/cc) =  7.8600              temperature(K) =   293.0",
        "    nuclide   atom-dens.   wgt. frac.      za      awt        title        temp",
        "      24050  7.11730E-04  7.51005E-03     24050    49.9460     cr-50         293.00",
        "      24052  1.37250E-02  1.50607E-01     24052    51.9405     cr-52         293.00",
        "      24053  1.55630E-03  1.74065E-02     24053    52.9407     cr-53         293.00",
        "      24054  3.87397E-04  4.41454E-03     24054    53.9389     cr-54         293.00",
        "      26054  3.66661E-03  4.17829E-02     26054    53.9396     fe-54         293.00",
        "      26056  5.75579E-02  6.80165E-01     26056    55.9349     fe-56         293.00",
        "      26057  1.32926E-03  1.59889E-02     26057    56.9354     fe-57         293.00",
        "      26058  1.76900E-04  2.16513E-03     26058    57.9333     fe-58         293.00",
        "      28058  4.38990E-03  5.37310E-02     28058    57.9353     ni-58         293.00",
        "      28060  1.69098E-03  2.14099E-02     28060    59.9308     ni-60         293.00",
        "      28061  7.35058E-05  9.46209E-04     28061    60.9311     ni-61         293.00",
        "      28062  2.34369E-04  3.06631E-03     28062    61.9283     ni-62         293.00",
        "      28064  5.96868E-05  8.06113E-04     28064    63.9280     ni-64         293.00",
        "",
        " mixture =     2          density(g/cc) = 0.12050E-02          temperature(K) =   293.0",
        "    nuclide   atom-dens.   wgt. frac.      za      awt        title        temp",
        "       6000  7.49187E-09  1.24000E-04      6000    12.0107     c         293.00",
        "       7014  3.89870E-05  7.52324E-01      7014    14.0031     n-14         293.00",
        "       7015  1.42431E-07  2.94416E-03      7015    15.0001     n-15         293.00",
        "       8016  1.04871E-05  2.31153E-01      8016    15.9949     o-16         293.00",
        "       8017  3.99481E-09  9.35803E-05      8017    16.9991     o-17         293.00",
        "       8018  2.15509E-08  5.34540E-04      8018    17.9992     o-18         293.00",
        "      18036  7.84073E-10  3.88624E-05     18036    35.9675     ar-36         293.00",
        "      18038  1.47261E-10  7.70385E-06     18038    37.9627     ar-38         293.00",
        "      18040  2.32077E-07  1.27804E-02     18040    39.9624     ar-40         293.00",
        "",
        " mixture =     3          density(g/cc) =  1.9895              temperature(K) =   293.0",
        "    nuclide   atom-dens.   wgt. frac.      za      awt        title        temp",
        "      13027  1.48301E-02  3.33969E-01     13027    26.9815     al-27         293.00",
        "      14028  4.09196E-04  9.55494E-03     14028    27.9769     si-28         293.00",
        "      14029  2.07875E-05  5.02741E-04     14029    28.9765     si-29         293.00",
        "      14030  1.37193E-05  3.43218E-04     14030    29.9738     si-30         293.00",
        "      24050  9.45040E-05  3.93956E-03     24050    49.9460     cr-50         293.00",
        "      24052  1.82242E-03  7.90042E-02     24052    51.9405     cr-52         293.00",
        "      24053  2.06647E-04  9.13094E-03     24053    52.9407     cr-53         293.00",
        "      24054  5.14389E-05  2.31574E-03     24054    53.9389     cr-54         293.00",
        "      26054  4.86672E-04  2.19099E-02     26054    53.9396     fe-54         293.00",
        "      26056  7.63971E-03  3.56662E-01     26056    55.9349     fe-56         293.00",
        "      26057  1.76434E-04  8.38419E-03     26057    56.9354     fe-57         293.00",
        "      26058  2.34802E-05  1.13534E-03     26058    57.9333     fe-58         293.00",
        "      28058  5.82673E-04  2.81751E-02     28058    57.9353     ni-58         293.00",
        "      28060  2.24445E-04  1.12268E-02     28060    59.9308     ni-60         293.00",
        "      28061  9.75645E-06  4.96166E-04     28061    60.9311     ni-61         293.00",
        "      28062  3.11078E-05  1.60789E-03     28062    61.9283     ni-62         293.00",
        "      28064  7.92225E-06  4.22703E-04     28064    63.9280     ni-64         293.00",
        "      92235  7.51882E-05  1.47501E-02     92235   235.0439     u-235         293.00",
        "      92238  5.86203E-04  1.16470E-01     92238   238.0508     u-238         293.00",
        "",
        "",
        "",
        "",
        "",
        " Cross section preparation time:  5.75 seconds",
    ]


@pytest.fixture
def single_mixture_ce_623(tmpdir):
    return [
        " mixture =     1          density(g/cc) =  7.8600              temperature(K) =   293.0",
        "    nuclide   atom-dens.   wgt. frac.      za      awt        title        temp",
        "      24050  7.11730E-04  7.51005E-03     24050    49.9460     cr-50         293.00",
        "      24052  1.37250E-02  1.50607E-01     24052    51.9405     cr-52         293.00",
        "      24053  1.55630E-03  1.74065E-02     24053    52.9407     cr-53         293.00",
        "      24054  3.87397E-04  4.41454E-03     24054    53.9389     cr-54         293.00",
        "      26054  3.66661E-03  4.17829E-02     26054    53.9396     fe-54         293.00",
        "      26056  5.75579E-02  6.80165E-01     26056    55.9349     fe-56         293.00",
        "      26057  1.32926E-03  1.59889E-02     26057    56.9354     fe-57         293.00",
        "      26058  1.76900E-04  2.16513E-03     26058    57.9333     fe-58         293.00",
        "      28058  4.38990E-03  5.37310E-02     28058    57.9353     ni-58         293.00",
        "      28060  1.69098E-03  2.14099E-02     28060    59.9308     ni-60         293.00",
        "      28061  7.35058E-05  9.46209E-04     28061    60.9311     ni-61         293.00",
        "      28062  2.34369E-04  3.06631E-03     28062    61.9283     ni-62         293.00",
        "      28064  5.96868E-05  8.06113E-04     28064    63.9280     ni-64         293.00",
        "",
    ]


@pytest.fixture
def mixing_table_multigroup_623(tmpdir):
    return [
        "                                                   mixing table",
        "",
        "                                          number of scattering angles =  3",
        "                                      cross section message threshold = 1.0E-01",
        "",
        "",
        " mixture =     1          density(g/cc) =  7.8600              temperature(K) =    293.00",
        "    nuclide    nucmix   atom-dens.   wgt. frac.     za      awt          temp               nuclide title",
        "      24050       1    7.11730E-04  7.51005E-03   24050    49.9460       293.00     cr50 2425 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:17:53 2014",
        "",
        "      24052       1    1.37250E-02  1.50607E-01   24052    51.9405       293.00     cr52 2431 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:17:53 2014",
        "",
        "      24053       1    1.55630E-03  1.74065E-02   24053    52.9407       293.00     cr53 2434 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:17:55 2014",
        "",
        "      24054       1    3.87397E-04  4.41454E-03   24054    53.9389       293.00     cr54 2437 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:17:55 2014",
        "",
        "      26054       1    3.66661E-03  4.17829E-02   26054    53.9396       293.00     fe54 2625 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:17:58 2014",
        "",
        "      26056       1    5.75579E-02  6.80165E-01   26056    55.9349       293.00     fe56 2631 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:17:58 2014",
        "",
        "      26057       1    1.32926E-03  1.59889E-02   26057    56.9354       293.00     fe57 2634 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:17:58 2014",
        "",
        "      26058       1    1.76900E-04  2.16513E-03   26058    57.9333       293.00     fe58 2637 endf/b-7 rel1 rev7 mod0 Mon Jun 16 16:17:58 2014",
        "",
        "      28058       1    4.38990E-03  5.37310E-02   28058    57.9353       293.00     ni58 2825 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:18:39 2014",
        "",
        "      28060       1    1.69098E-03  2.14099E-02   28060    59.9308       293.00     ni60 2831 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:18:39 2014",
        "",
        "      28061       1    7.35058E-05  9.46209E-04   28061    60.9311       293.00     ni61 2834 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:18:39 2014",
        "",
        "      28062       1    2.34369E-04  3.06631E-03   28062    61.9283       293.00     ni62 2837 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:18:39 2014",
        "",
        "      28064       1    5.96868E-05  8.06113E-04   28064    63.9280       293.00     ni64 2843 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:18:39 2014",
        "",
        "",
        " mixture =     2          density(g/cc) = 0.12050E-02          temperature(K) =    293.00",
        "    nuclide    nucmix   atom-dens.   wgt. frac.     za      awt          temp               nuclide title",
        "       6000       2    7.49187E-09  1.23999E-04    6000    12.0107       293.00     c 600 endf/b-7 rel1 rev7 mod0 Mon Jun 16 16:17:50 2014",
        "",
        "       7014       2    3.89870E-05  7.52320E-01    7014    14.0031       293.00     n14 725 endf/b-7 rel1 rev7 mod0 Mon Jun 16 16:18:39 2014",
        "",
        "       7015       2    1.42431E-07  2.94415E-03    7015    15.0001       293.00     n15 728 endf/b-7 rel1 rev7 mod0 Mon Jun 16 16:18:39 2014",
        "",
        "       8016       2    1.04871E-05  2.31152E-01    8016    15.9949       293.00     o16 825 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:18:40 2014",
        "",
        "       8017       2    3.99481E-09  9.35799E-05    8017    16.9991       293.00     o17 828 endf/b-7 rel1 rev7 mod0 Mon Jun 16 16:18:40 2014",
        "",
        "       8018       2    2.15509E-08  5.39169E-04    8018    18.1551       293.00     Injected O-18 zero cross sections",
        "      18036       2    7.84073E-10  3.88622E-05   18036    35.9675       293.00     ar36 1825 endf/b-7 rel1 rev7 mod0 Mon Jun 16 16:17:47 2014",
        "",
        "      18038       2    1.47261E-10  7.70382E-06   18038    37.9627       293.00     ar38 1831 endf/b-7 rel1 rev7 mod0 Mon Jun 16 16:17:47 2014",
        "",
        "      18040       2    2.32077E-07  1.27804E-02   18040    39.9624       293.00     ar40 1837 endf/b-7 rel1 rev7 mod2 Mon Jun 16 16:17:47 2014",
        "",
        "",
        " mixture =     3          density(g/cc) =  1.9895              temperature(K) =    293.00",
        "    nuclide    nucmix   atom-dens.   wgt. frac.     za      awt          temp               nuclide title",
        "      13027       3    1.48301E-02  3.33969E-01   13027    26.9815       293.00     al27 1325 endf/b-7 rel1 rev7 mod1 Mon Jun 16 16:17:47 2014",
        "",
        "      14028       3    4.09196E-04  9.55494E-03   14028    27.9769       293.00     si28 1425 endf/b-7 rel1 rev7 mod1 Mon Jun 16 16:18:44 2014",
        "",
        "      14029       3    2.07875E-05  5.02740E-04   14029    28.9765       293.00     si29 1428 endf/b-7 rel1 rev7 mod3 Mon Jun 16 16:18:44 2014",
        "",
        "      14030       3    1.37193E-05  3.43218E-04   14030    29.9738       293.00     si30 1431 endf/b-7 rel1 rev7 mod2 Mon Jun 16 16:18:44 2014",
        "",
        "      24050       3    9.45040E-05  3.93956E-03   24050    49.9460       293.00     cr50 2425 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:17:53 2014",
        "",
        "      24052       3    1.82242E-03  7.90042E-02   24052    51.9405       293.00     cr52 2431 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:17:53 2014",
        "",
        "      24053       3    2.06647E-04  9.13094E-03   24053    52.9407       293.00     cr53 2434 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:17:55 2014",
        "",
        "      24054       3    5.14389E-05  2.31574E-03   24054    53.9389       293.00     cr54 2437 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:17:55 2014",
        "",
        "      26054       3    4.86672E-04  2.19099E-02   26054    53.9396       293.00     fe54 2625 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:17:58 2014",
        "",
        "      26056       3    7.63971E-03  3.56662E-01   26056    55.9349       293.00     fe56 2631 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:17:58 2014",
        "",
        "      26057       3    1.76434E-04  8.38420E-03   26057    56.9354       293.00     fe57 2634 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:17:58 2014",
        "",
        "      26058       3    2.34802E-05  1.13534E-03   26058    57.9333       293.00     fe58 2637 endf/b-7 rel1 rev7 mod0 Mon Jun 16 16:17:58 2014",
        "",
        "      28058       3    5.82673E-04  2.81751E-02   28058    57.9353       293.00     ni58 2825 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:18:39 2014",
        "",
        "      28060       3    2.24445E-04  1.12268E-02   28060    59.9308       293.00     ni60 2831 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:18:39 2014",
        "",
        "      28061       3    9.75645E-06  4.96166E-04   28061    60.9311       293.00     ni61 2834 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:18:39 2014",
        "",
        "      28062       3    3.11078E-05  1.60789E-03   28062    61.9283       293.00     ni62 2837 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:18:39 2014",
        "",
        "      28064       3    7.92225E-06  4.22703E-04   28064    63.9280       293.00     ni64 2843 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:18:39 2014",
        "",
        "      92235       3    7.51882E-05  1.47501E-02   92235   235.0439       293.00     u235 9228 endf/b-7 rel1 rev7 mod7 Mon Jun 16 16:18:34 2014",
        "",
        "      92238       3    5.86203E-04  1.16470E-01   92238   238.0508       293.00     u238 9237 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:18:34 2014",
        "",
        "",
        "",
        "",
        " ",
        "  ***** warning ***** sggp message number k6-064 follows:",
    ]


@pytest.fixture
def single_mixture_multigroup_623(tmpdir):
    return [
        " mixture =     1          density(g/cc) =  7.8600              temperature(K) =    293.00",
        "    nuclide    nucmix   atom-dens.   wgt. frac.     za      awt          temp               nuclide title",
        "      24050       1    7.11730E-04  7.51005E-03   24050    49.9460       293.00     cr50 2425 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:17:53 2014",
        "",
        "      24052       1    1.37250E-02  1.50607E-01   24052    51.9405       293.00     cr52 2431 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:17:53 2014",
        "",
        "      24053       1    1.55630E-03  1.74065E-02   24053    52.9407       293.00     cr53 2434 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:17:55 2014",
        "",
        "      24054       1    3.87397E-04  4.41454E-03   24054    53.9389       293.00     cr54 2437 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:17:55 2014",
        "",
        "      26054       1    3.66661E-03  4.17829E-02   26054    53.9396       293.00     fe54 2625 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:17:58 2014",
        "",
        "      26056       1    5.75579E-02  6.80165E-01   26056    55.9349       293.00     fe56 2631 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:17:58 2014",
        "",
        "      26057       1    1.32926E-03  1.59889E-02   26057    56.9354       293.00     fe57 2634 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:17:58 2014",
        "",
        "      26058       1    1.76900E-04  2.16513E-03   26058    57.9333       293.00     fe58 2637 endf/b-7 rel1 rev7 mod0 Mon Jun 16 16:17:58 2014",
        "",
        "      28058       1    4.38990E-03  5.37310E-02   28058    57.9353       293.00     ni58 2825 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:18:39 2014",
        "",
        "      28060       1    1.69098E-03  2.14099E-02   28060    59.9308       293.00     ni60 2831 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:18:39 2014",
        "",
        "      28061       1    7.35058E-05  9.46209E-04   28061    60.9311       293.00     ni61 2834 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:18:39 2014",
        "",
        "      28062       1    2.34369E-04  3.06631E-03   28062    61.9283       293.00     ni62 2837 endf/b-7 rel1 rev7 mod5 Mon Jun 16 16:18:39 2014",
        "",
        "      28064       1    5.96868E-05  8.06113E-04   28064    63.9280       293.00     ni64 2843 endf/b-7 rel1 rev7 mod4 Mon Jun 16 16:18:39 2014",
        "",
        "",
    ]

#####################################################################
# End of Fixtures --------------------------------------------------#
#####################################################################


def test_object_created(ce_623_file):
    # arrange
    path = "scale_examples/cylinder_ce.out"
    sf = 1234
    # act
    case = EddySCALECase(filepath=path, scaling_factor=sf, file=ce_623_file)
    # assert
    assert case


def test_get_runtime(simple_case):
    # arrange
    # act
    rundate, runtime = simple_case.get_runtime()
    # assert
    assert type(rundate) == str
    assert type(runtime) == str
    assert len(rundate) == 10  # yyyy/mm/dd
    assert len(runtime) == 8  # hh:mm:ss


def test_get_input(simple_case):
    # arrange
    # act
    actual_input = simple_case.get_input()
    # assert
    assert actual_input[0] == "      Example Cylinder Source"
    assert actual_input[-1] == 'end'
    assert len(actual_input) == 392


def test_get_tally_data():
    # todo: implement
    pass


def test_create_tallies():
    # todo: implement
    pass


def test_scale_tally_results_with_scaling_factor(simple_case, mocker):
    # arrange
    class MockTally(eddy_scale_case.Tally):
        def __init__(self):
            pass
    tally_mock = mocker.patch('eddymc_core.scale.eddy_scale_case.Tally.scale_results')
    case = simple_case
    simple_case.tally_list = [MockTally(), MockTally(), MockTally()]
    # act
    case.scale_tally_results()
    # assert
    tally_mock.assert_called()
    assert tally_mock.call_count == 3
    assert tally_mock.call_args_list[0][0][0] == 1234
    assert tally_mock.call_args_list[1][0][0] == 1234
    assert tally_mock.call_args_list[2][0][0] == 1234


def test_scale_tally_results_with_scaling_factor_of_1(mocker):
    # arrange
    case = MockEddySCALECase(
        filepath="scale_examples/cylinder_ce.out",
        scaling_factor=1,
        file=ce_623_file,
    )
    tally_mock = mocker.patch('eddymc_core.scale.eddy_scale_case.Tally.scale_results')
    # act
    case.scale_tally_results()
    # assert
    tally_mock.assert_not_called()


def test_get_mixture_data(simple_case):
    # arrange
    # act
    output_623 = simple_case.get_mixture_data()
    # assert
    assert len(output_623) == 56


def test_get_mixture_data_ce(ce_623_file, ce_624_file):
    # arrange
    case_623 = MockEddySCALECase(
        filepath="scale_examples/cylinder_ce.out",
        scaling_factor=1234,
        file=ce_623_file,
    )
    case_624 = MockEddySCALECase(
        filepath="scale_examples/cylinder_ce.out",
        scaling_factor=1234,
        file=ce_624_file,
    )
    # act
    output_623 = case_623.get_mixture_data()
    output_624 = case_624.get_mixture_data()
    # assert
    assert len(output_623) == 56
    assert len(output_624) == 56


def test_get_mixture_data_multigroup(multigroup_623_file, multigroup_624_file):
    # arrange
    case_623 = MockEddySCALECase(
        filepath="scale_examples/cylinder_ce.out",
        scaling_factor=1234,
        file=multigroup_623_file,
    )
    case_624 = MockEddySCALECase(
        filepath="scale_examples/cylinder_ce.out",
        scaling_factor=1234,
        file=multigroup_624_file,
    )
    # act
    output_623 = case_623.get_mixture_data()
    output_624 = case_624.get_mixture_data()
    # assert
    assert len(output_623) == 99
    assert len(output_624) == 99


def test_create_mixtures_ce_623(simple_case, mixing_table_ce_623, single_mixture_ce_623, mocker):
    # arrange
    mocked_Mixture = mocker.patch('eddymc_core.scale.eddy_scale_case.Mixture')
    case_623 = simple_case
    # act
    mixture_list = case_623.create_mixtures(mixing_table_ce_623)
    # assert
    assert len(mixture_list) == 3
    mocked_Mixture.assert_called()
    assert mocked_Mixture.call_count == 3
    assert mocked_Mixture.call_args_list[0][0][0] == single_mixture_ce_623


def test_create_mixtures_multigroup_623(multigroup_case, mixing_table_multigroup_623, single_mixture_multigroup_623, mocker):
    # arrange
    mocked_Mixture = mocker.patch('eddymc_core.scale.eddy_scale_case.Mixture')
    # act
    mixture_list = multigroup_case.create_mixtures(mixing_table_multigroup_623)
    # assert
    mocked_Mixture.assert_called()
    assert len(mixture_list) == 3
    assert mocked_Mixture.call_count == 3      # checks correct number of mixtures found
    assert mocked_Mixture.call_args_list[0][0][0] == single_mixture_multigroup_623  # checks first mixture is correct
