import unittest
import numpy as np
import pumapy as puma
import os
test_dir = os.path.dirname(os.path.abspath(__file__))


class TestImportExportVTKI(unittest.TestCase):

    def test_io_vti_ws(self):
        ws = puma.Workspace.from_shape_value((10, 11, 12), 34)
        ws.matrix[0, -1, 0] = 1
        ws.matrix[0, 0, -1] = 2
        ws.matrix[-1, -1, -1] = 3
        ws.matrix[-1, 0, 0] = 4
        puma.export_vti(os.path.join(test_dir, "out", "ws1"), ws)
        np.testing.assert_equal("ws1.vti" in os.listdir(os.path.join(test_dir, "out")), True)
        ws2 = ws.copy()
        ws = puma.import_vti(os.path.join(test_dir, "out", "ws1.vti"))
        np.testing.assert_equal(ws.matrix, ws2.matrix)

    def test_io_vti_nparray(self):
        nparray = np.full((10, 11, 12), 34, dtype=np.uint16)
        nparray[0, -1, 0] = 1
        nparray[0, 0, -1] = 2
        nparray[-1, -1, -1] = 3
        nparray[-1, 0, 0] = 4
        puma.export_vti(os.path.join(test_dir, "out", "nparray1"), nparray)
        np.testing.assert_equal("nparray1.vti" in os.listdir(os.path.join(test_dir, "out")), True)
        nparray2 = nparray.copy()
        nparray = puma.import_vti(os.path.join(test_dir, "out", "nparray1.vti"), import_ws=False)["data"]
        np.testing.assert_equal(nparray, nparray2)

    def test_io_vti_2Dnparray(self):
        nparray = np.full((10, 11), 34, dtype=np.uint16)
        nparray[0, -1] = 1
        nparray[-1, -1] = 3
        nparray[-1, 0] = 4
        puma.export_vti(os.path.join(test_dir, "out", "nparray2"), nparray)
        np.testing.assert_equal("nparray2.vti" in os.listdir(os.path.join(test_dir, "out")), True)
        nparray2 = np.expand_dims(nparray.copy(), axis=2)
        nparray = puma.import_vti(os.path.join(test_dir, "out", "nparray2.vti"), import_ws=False)["data"]
        np.testing.assert_equal(nparray, nparray2)

    def test_io_vti_nparray_orientation(self):
        nparray = np.tile((1, 0, 0), (5, 10, 20, 1)).astype(float)
        nparray[0, -1, 0] = [0, 1, 0]
        nparray[0, 0, -1] = [0, 0, 1]
        nparray[-1, -1, -1] = [10, 10, 10]
        nparray[-1, 0, 0] = [10, 0, 1]
        puma.export_vti(os.path.join(test_dir, "out", "nparray3"), nparray)
        np.testing.assert_equal("nparray3.vti" in os.listdir(os.path.join(test_dir, "out")), True)
        nparray2 = nparray.copy()
        nparray = puma.import_vti(os.path.join(test_dir, "out", "nparray3.vti"), import_ws=False)["data_orient"]
        np.testing.assert_equal(nparray, nparray2)

    def test_io_vti_orientation(self):
        ws = puma.Workspace.from_shape_value_vector((5, 10, 20), 47, (1, 0, 0))
        ws.orientation[0, -1, 0] = [0, 1, 0]
        ws.orientation[0, 0, -1] = [0, 0, 1]
        ws.orientation[-1, -1, -1] = [10, 10, 10]
        ws.orientation[-1, 0, 0] = [10, 0, 1]
        puma.export_vti(os.path.join(test_dir, "out", "ws2"), ws)
        np.testing.assert_equal("ws2.vti" in os.listdir(os.path.join(test_dir, "out")), True)
        ws2 = ws.copy()
        ws = puma.import_vti(os.path.join(test_dir, "out", "ws2.vti"))
        np.testing.assert_equal(ws.orientation, ws2.orientation)
        np.testing.assert_equal(ws.matrix, ws2.matrix)

    def test_io_vtk_ws(self):
        # Created as:
        # puma::MatVec3<double> dirs(10, 11, 7, puma::Vec3<double>(1, 0, 0));
        # dirs.at(1, 2, 3) = puma::Vec3<double>(1, 2, 3);
        # dirs.at(7, 6, 5) = puma::Vec3<double>(7, 6, 5);
        # dirs.at(3, 10, 2) = puma::Vec3<double>(3, 10, 2);
        orient_test = puma.import_vti(os.path.join(test_dir, "testdata", "orient_test.vtk"), import_ws=False)["PuMA_Vec3"]
        nparray = np.tile((1, 0, 0), (10, 11, 7, 1)).astype(float)
        nparray[1, 2, 3] = [1, 2, 3]
        nparray[7, 6, 5] = [7, 6, 5]
        nparray[3, 10, 2] = [3, 10, 2]
        np.testing.assert_equal(orient_test, nparray)


class TestImportExport3Dtiff(unittest.TestCase):

    def test_export_3Dtiff_ws(self):
        ws = puma.Workspace.from_shape_value((10, 11, 12), 34)
        ws.matrix[0, -1, 0] = 1
        ws.matrix[0, 0, -1] = 2
        ws.matrix[-1, -1, -1] = 3
        ws.matrix[-1, 0, 0] = 4
        puma.export_3Dtiff(os.path.join(test_dir, "out", "ws"), ws)
        np.testing.assert_equal("ws.tif" in os.listdir(os.path.join(test_dir, "out")), True)

    def test_import_3Dtiff_ws(self):
        ws = puma.import_3Dtiff(os.path.join(test_dir, "out", "ws.tif"))
        ws2 = puma.Workspace.from_shape_value((10, 11, 12), 34)
        ws2.matrix[0, -1, 0] = 1
        ws2.matrix[0, 0, -1] = 2
        ws2.matrix[-1, -1, -1] = 3
        ws2.matrix[-1, 0, 0] = 4
        np.testing.assert_equal(ws.matrix, ws2.matrix)

    def test_export_3Dtiff_nparray(self):
        nparray = np.full((10, 11, 12), 34, dtype=np.uint16)
        nparray[0, -1, 0] = 1
        nparray[0, 0, -1] = 2
        nparray[-1, -1, -1] = 3
        nparray[-1, 0, 0] = 4
        puma.export_3Dtiff(os.path.join(test_dir, "out", "nparray"), nparray)
        np.testing.assert_equal("nparray.tif" in os.listdir(os.path.join(test_dir, "out")), True)

    def test_import_3Dtiff_nparray(self):
        nparray = puma.import_3Dtiff(os.path.join(test_dir, "out", "nparray.tif"), import_ws=False)
        nparray2 = np.full((10, 11, 12), 34, dtype=np.uint16)
        nparray2[0, -1, 0] = 1
        nparray2[0, 0, -1] = 2
        nparray2[-1, -1, -1] = 3
        nparray2[-1, 0, 0] = 4
        np.testing.assert_equal(nparray, nparray2)


class TestImportExportbin(unittest.TestCase):

    def test_export_bin_ws(self):
        ws = puma.Workspace.from_shape_value((10, 11, 12), 34)
        ws.matrix[0, -1, 0] = 1
        ws.matrix[0, 0, -1] = 2
        ws.matrix[-1, -1, -1] = 3
        ws.matrix[-1, 0, 0] = 4
        puma.export_bin(os.path.join(test_dir, "out", "ws"), ws)
        np.testing.assert_equal("ws.pumapy" in os.listdir(os.path.join(test_dir, "out")), True)

    def test_import_bin_ws(self):
        ws = puma.import_bin(os.path.join(test_dir, "out", "ws.pumapy"))
        ws2 = puma.Workspace.from_shape_value((10, 11, 12), 34)
        ws2.matrix[0, -1, 0] = 1
        ws2.matrix[0, 0, -1] = 2
        ws2.matrix[-1, -1, -1] = 3
        ws2.matrix[-1, 0, 0] = 4
        np.testing.assert_equal(ws.matrix, ws2.matrix)


if __name__ == '__main__':
    unittest.main()
