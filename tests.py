import unittest
from src.function import convertXMLtoCSV, convertXMLtoXLSX, saveXML
import os

class TestXMLConversion(unittest.TestCase):

    def test_convertXMLtoCSV(self):
        # Test case for convertXMLtoCSV function
        # Define input parameters
        pathXML = 'G:/Atila_Rocha/Programacao/HydroDataViewer/db/xml'
        xml_file = 'G:/Atila_Rocha/Programacao/HydroDataViewer/db/xml/Estacao_33281000_de_15_06_2023_a_15_06_2023.xml'
        codigoEstacao = '33281000'
        dataInicio = '15/06/2023'
        dataFim = '15/06/2023'
        pathCSV = 'G:/Atila_Rocha/Programacao/HydroDataViewer/db/csv'

        # Execute the function
        convertXMLtoCSV(pathXML, xml_file, codigoEstacao, dataInicio, dataFim, pathCSV)

        # Assert the expected result
        expected_csv_path = 'G:/Atila_Rocha/Programacao/HydroDataViewer/db/csv/Estacao_33281000_de_15_06_2023_a_15_06_2023.csv'
        self.assertTrue(os.path.exists(expected_csv_path))

    def test_convertXMLtoXLSX(self):
        # Test case for convertXMLtoXLSX function
        # Define input parameters
        pathXML = 'G:/Atila_Rocha/Programacao/HydroDataViewer/db/xml'
        xml_file = 'G:/Atila_Rocha/Programacao/HydroDataViewer/db/xml/Estacao_33281000_de_15_06_2023_a_15_06_2023.xml'
        codigoEstacao = '33281000'
        dataInicio = '15/06/2023'
        dataFim = '15/06/2023'
        pathXLSX = 'G:/Atila_Rocha/Programacao/HydroDataViewer/db/xlsx'

        # Execute the function
        convertXMLtoXLSX(pathXML, xml_file, codigoEstacao, dataInicio, dataFim, pathXLSX)

        # Assert the expected result
        expected_xlsx_path = 'G:/Atila_Rocha/Programacao/HydroDataViewer/db/xlsx/Estacao_33281000_de_15_06_2023_a_15_06_2023.xlsx'
        self.assertTrue(os.path.exists(expected_xlsx_path))

if __name__ == '__main__':
    unittest.main()
