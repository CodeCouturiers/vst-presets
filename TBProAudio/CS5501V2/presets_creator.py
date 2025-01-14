import os
import xml.etree.ElementTree as ET
from xml.dom import minidom
import pathlib


class CS5501Parameters:
    PARAMETERS = {
        # Basic settings
        "GUI Scale": "1.000000",
        "Toggle Tooltips": "1.000000",
        "OS Off/2x/4x": "0.000000",
        "ByPass Off/On": "0.000000",
        "AB-LM Lite Mode": "0.000000",

        # Phase settings
        "Phase0 Invert Off/On": "0.000000",
        "Phase1 Invert Off/On": "0.000000",

        # Volume settings
        "In Volume L": "-0.000000",
        "In Volume R": "-0.000000",
        "Link In Volume Off/On": "1.000000",
        "Out Volume L": "-0.000000",
        "Out Volume R": "-0.000000",
        "Link Out Volume Off/On": "1.000000",
        "Link In/Out Volume Off/On": "0.000000",

        # Clip settings
        "Clip Off/On": "0.000000",
        "Clip Ceiling": "-0.100000",

        # Meter settings
        "Meter Display Mode": "0.000000",
        "Meter Mode": "4.000000",
        "VU Reference": "-18.000000",
        "EBU SL Reference": "-23.000000",
        "EBU ML Reference": "-23.000000",
        "RMS Reference": "-18.000000",
        "PEAK Reference": "0.000000",

        # Monitor settings
        "Monitor Mode 0": "0.000000",
        "Monitor Mode 1": "0.000000",

        # Position settings
        "Pos0": "0.000000",
        "Pos1": "1.000000",
        "Pos2": "2.000000",
        "Pos3": "3.000000",
        "Pos4": "4.000000",
        "Pos5": "5.000000",
        "Pos6": "6.000000",
        "Pos7": "7.000000",
        "Pos8": "8.000000",
        "Pos9": "9.000000",
        "Pos10": "10.000000",
        "Pos11": "11.000000",
        "Pos12": "12.000000",

        # Display settings
        "EQ Display Mode": "0.000000",
        "Module Display Mode": "4.000000",

        # Filter0 settings
        "Filter0 Off/On": "1.000000",
        "Filter0 Stereo Placement": "0.000000",
        "Filter0 Solo Off/On": "0.000000",
        "Filter0 HP Off/On": "0.000000",
        "Filter0 HP F": "30.000000",
        "Filter0 HP Slope 6-48dB": "0.000000",
        "Filter0 LP Off/On": "0.000000",
        "Filter0 LP F": "20000.000000",
        "Filter0 LP Slope 6-48dB": "0.000000",
        "Filter0 HF Off/On": "0.000000",
        "Filter0 HF Type": "0.000000",
        "Filter0 HF F": "12000.000000",
        "Filter0 HF G": "0.000000",
        "Filter0 HF Q": "0.700000",
        "Filter0 HF Solo": "0.000000",
        "Filter0 HMF Off/On": "0.000000",
        "Filter0 HMF F": "6000.000000",
        "Filter0 HMF G": "0.000000",
        "Filter0 HMF Q": "0.700000",
        "Filter0 HMF Solo": "0.000000",
        "Filter0 MF Off/On": "0.000000",
        "Filter0 MF F": "1500.000000",
        "Filter0 MF G": "0.000000",
        "Filter0 MF Q": "0.700000",
        "Filter0 MF Solo": "0.000000",
        "Filter0 LMF Off/On": "0.000000",
        "Filter0 LMF F": "250.000000",
        "Filter0 LMF G": "0.000000",
        "Filter0 LMF Q": "0.700000",
        "Filter0 LMF Solo": "0.000000",
        "Filter0 LF Off/On": "0.000000",
        "Filter0 LF Type": "0.000000",
        "Filter0 LF F": "150.000000",
        "Filter0 LF G": "0.000000",
        "Filter0 LF Q": "0.700000",
        "Filter0 LF Solo": "0.000000",

        # Filter1 settings (identical structure to Filter0)
        "Filter1 Off/On": "0.000000",
        "Filter1 Stereo Placement": "0.000000",
        "Filter1 Solo Off/On": "0.000000",
        "Filter1 HP Off/On": "0.000000",
        "Filter1 HP F": "30.000000",
        "Filter1 HP Slope 6-48dB": "0.000000",
        "Filter1 LP Off/On": "0.000000",
        "Filter1 LP F": "20000.000000",
        "Filter1 LP Slope 6-48dB": "0.000000",
        "Filter1 HF Off/On": "0.000000",
        "Filter1 HF Type": "0.000000",
        "Filter1 HF F": "12000.000000",
        "Filter1 HF G": "0.000000",
        "Filter1 HF Q": "0.700000",
        "Filter1 HF Solo": "0.000000",
        "Filter1 HMF Off/On": "0.000000",
        "Filter1 HMF F": "6000.000000",
        "Filter1 HMF G": "0.000000",
        "Filter1 HMF Q": "0.700000",
        "Filter1 HMF Solo": "0.000000",
        "Filter1 MF Off/On": "0.000000",
        "Filter1 MF F": "1500.000000",
        "Filter1 MF G": "0.000000",
        "Filter1 MF Q": "0.700000",
        "Filter1 MF Solo": "0.000000",
        "Filter1 LMF Off/On": "0.000000",
        "Filter1 LMF F": "250.000000",
        "Filter1 LMF G": "0.000000",
        "Filter1 LMF Q": "0.700000",
        "Filter1 LMF Solo": "0.000000",
        "Filter1 LF Off/On": "0.000000",
        "Filter1 LF Type": "0.000000",
        "Filter1 LF F": "150.000000",
        "Filter1 LF G": "0.000000",
        "Filter1 LF Q": "0.700000",
        "Filter1 LF Solo": "0.000000",

        # Compressor 0 settings
        "Comp0 Off/On": "0.000000",
        "Comp0 Stereo Placement": "0.000000",
        "Comp0 Solo Off/On": "0.000000",
        "Comp0 Comp1 link": "0.000000",
        "Comp0 SC Mode In/Ext": "0.000000",
        "Comp0 SC Monitor Off/On": "0.000000",
        "Comp0 SC LC Off/On": "0.000000",
        "Comp0 SC LC Slope": "0.000000",
        "Comp0 SC LC F": "300.000000",
        "Comp0 SC HC Off/On": "0.000000",
        "Comp0 SC HC Slope": "0.000000",
        "Comp0 SC HC F": "3400.000000",
        "Comp0 SC LC/HC Link": "0.000000",
        "Comp0 Type": "0.000000",
        "Comp0 Threshold": "0.000000",
        "Comp0 Attack": "10.000000",
        "Comp0 Release": "0.100000",
        "Comp0 Ratio": "2.000000",
        "Comp0 Auto release": "0.000000",
        "Comp0 MakeUpGain": "0.000000",
        "Comp0 Mix": "100.000000",

        # Compressor 1 settings
        "Comp1 Off/On": "0.000000",
        "Comp1 Stereo Placement": "0.000000",
        "Comp1 Solo Off/On": "0.000000",
        "Comp1 SC Mode In/Ext": "0.000000",
        "Comp1 SC Monitor Off/On": "0.000000",
        "Comp1 SC LC Off/On": "0.000000",
        "Comp1 SC LC Slope": "0.000000",
        "Comp1 SC LC F": "300.000000",
        "Comp1 SC HC Off/On": "0.000000",
        "Comp1 SC HC Slope": "0.000000",
        "Comp1 SC HC F": "3400.000000",
        "Comp1 SC LC/HC Link": "0.000000",
        "Comp1 Type": "0.000000",
        "Comp1 Threshold": "0.000000",
        "Comp1 Attack": "10.000000",
        "Comp1 Release": "0.100000",
        "Comp1 Ratio": "2.000000",
        "Comp1 Auto release": "0.000000",
        "Comp1 MakeUpGain": "0.000000",
        "Comp1 Mix": "100.000000",

        # Gate 0 settings
        "Gate0 Off/On": "0.000000",
        "Gate0 Stereo Placement": "0.000000",
        "Gate0 Solo Off/On": "0.000000",
        "Gate0 Gate1 link": "0.000000",
        "Gate0 SC Mode In/Ext": "0.000000",
        "Gate0 SC Monitor Off/On": "0.000000",
        "Gate0 SC LC Off/On": "0.000000",
        "Gate0 SC LC Slope": "0.000000",
        "Gate0 SC LC F": "300.000000",
        "Gate0 SC HC Off/On": "0.000000",
        "Gate0 SC HC Slope": "0.000000",
        "Gate0 SC HC F": "3400.000000",
        "Gate0 SC LC/HC Link": "0.000000",
        "Gate0 Threshold": "-60.000000",
        "Gate0 Attack": "5.000000",
        "Gate0 Hold": "50.000000",
        "Gate0 Release": "100.000000",
        "Gate0 Mode Gate/Exp.": "0.000000",
        "Gate0 Range": "-72.000000",

        # Gate 1 settings
        "Gate1 Off/On": "0.000000",
        "Gate1 Stereo Placement": "0.000000",
        "Gate1 Solo Off/On": "0.000000",
        "Gate1 SC Mode In/Ext": "0.000000",
        "Gate1 SC Monitor Off/On": "0.000000",
        "Gate1 SC LC Off/On": "0.000000",
        "Gate1 SC LC Slope": "0.000000",
        "Gate1 SC LC F": "300.000000",
        "Gate1 SC HC Off/On": "0.000000",
        "Gate1 SC HC Slope": "0.000000",
        "Gate1 SC HC F": "3400.000000",
        "Gate1 SC LC/HC Link": "0.000000",
        "Gate1 Threshold": "-60.000000",
        "Gate1 Attack": "5.000000",
        "Gate1 Hold": "50.000000",
        "Gate1 Release": "100.000000",
        "Gate1 Mode Gate/Exp.": "0.000000",
        "Gate1 Range": "-72.000000",

        # De-esser 0 settings
        "Dees0 Off/On": "0.000000",
        "Dees0 Stereo Placement": "0.000000",
        "Dees0 Solo Off/On": "0.000000",
        "Dees0 Dees1 link": "0.000000",
        "Dees0 SC Mode In/Ext": "0.000000",
        "Dees0 SC Monitor Off/On": "0.000000",
        "Dees0 SC LC Off/On": "0.000000",
        "Dees0 SC LC Slope": "0.000000",
        "Dees0 SC LC F": "300.000000",
        "Dees0 SC HC Off/On": "0.000000",
        "Dees0 SC HC Slope": "0.000000",
        "Dees0 SC HC F": "3400.000000",
        "Deess0 SC LC/HC Link": "0.000000",
        "Dees0 Type": "1.000000",
        "Dees0 Wide Band Off/On": "0.000000",
        "Dees0 Frequency": "8000.000000",
        "Dees0 Q": "0.700000",
        "Dees0 Gain": "0.000000",
        "Dees0 Threshold": "0.000000",
        "Dees0 Ratio": "2.000000",
        "Dees0 Attack": "2.000000",
        "Dees0 Release": "50.000000",
        "Dees0 Range": "-6.000000",
        "Dees0 Output": "0.000000",
        "Dees0 Listen Mode": "0.000000",

        # De-esser 1 settings
        "Dees1 Off/On": "0.000000",
        "Dees1 Stereo Placement": "0.000000",
        "Dees1 Solo Off/On": "0.000000",
        "Dees1 SC Mode In/Ext": "0.000000",
        "Dees1 SC Monitor Off/On": "0.000000",
        "Dees1 SC LC Off/On": "0.000000",
        "Dees1 SC LC Slope": "0.000000",
        "Dees1 SC LC F": "300.000000",
        "Dees1 SC HC Off/On": "0.000000",
        "Dees1 SC HC Slope": "0.000000",
        "Dees1 SC HC F": "3400.000000",
        "Dees1 SC LC/HC Link": "0.000000",
        "Dees1 Type": "1.000000",
        "Dees1 Wide Band Off/On": "0.000000",
        "Dees1 Frequency": "10000.000000",
        "Dees1 Q": "0.700000",
        "Dees1 Gain": "0.000000",
        "Dees1 Threshold": "0.000000",
        "Dees1 Ratio": "2.000000",
        "Dees1 Attack": "2.000000",
        "Dees1 Release": "50.000000",
        "Dees1 Range": "-6.000000",
        "Dees1 Output": "0.000000",
        "Dees1 Listen Mode": "0.000000",

        # Limiter 0 settings
        "Limit0 Off/On": "0.000000",
        "Limit0 Stereo Placement": "0.000000",
        "Limit0 Solo Off/On": "0.000000",
        "Limit0 Limit1 link": "0.000000",
        "Limit0 Gain": "0.000000",
        "Limit0 Release": "50.000000",
        "Limit0 Auto release": "1.000000",
        "Limit0 Ceiling": "-0.100000",

        # Limiter 1 settings
        "Limit1 Off/On": "0.000000",
        "Limit1 Stereo Placement": "0.000000",
        "Limit1 Solo Off/On": "0.000000",
        "Limit1 Gain": "0.000000",
        "Limit1 Release": "50.000000",
        "Limit1 Auto release": "1.000000",
        "Limit1 Ceiling": "-0.100000",

        # Saturation settings
        "Saturation Off/On": "0.000000",
        "Saturation Stereo Placement": "0.000000",
        "Saturation Solo Off/On": "0.000000",
        "Saturation Mode": "0.000000",
        "Saturation Stages": "1.000000",
        "Saturation Even Harmonics": "0.000000",
        "Saturation Odd Harmonics": "0.000000",
        "Saturation Fluctuation": "0.000000",
        "Saturation Mix": "100.000000",

        # Additional settings
        "Analog Off/On": "0.000000",
        "Theme": "0.000000",
        "Enable EQ Component Tolerances": "0.000000",
        "Hide Knob Overlay Text": "0.000000",
        "Force Mono Mode": "0.000000",
        "Online Update Check": "1.000000",
        "ABLMLiteGain": "0.000000",
        "Clip Position": "0.000000",
        "AB-LM Lite Start Position": "0.000000",
        "AB-LM Lite End Position": "0.000000",
        "Smart silence processing": "0.000000",
        "SSP custom threshold": "-180.000000",
        "display configuration": "0.000000",

        # Oscilloscope settings
        "Oscilloscope zoom time": "100.000000",
        "Oscilloscope offset time": "0.000000",
        "Oscilloscope zoom mag": "100.000000",
        "Oscilloscope config page": "0.000000",
        "Oscilloscope pause": "0.000000",
        "Oscilloscope signal mode": "0.000000",
        "Oscilloscope show IN": "1.000000",
        "Oscilloscope show SC": "0.000000",
        "Oscilloscope show OUT": "1.000000",
        "Oscilloscope loop Length": "1000.000000",

        # Spectrum analyzer settings
        "Spectrum analyzer zoom freq": "100.000000",
        "Spectrum analyzer offset freq": "0.000000",
        "Spectrum analyzer zoom mag": "100.000000",
        "Spectrum analyzer offset mag": "0.000000",
        "Spectrum analyzer zoom EQ": "100.000000",
        "Spectrum analyzer config page": "0.000000",
        "Spectrum analyzer show IN": "1.000000",
        "Spectrum analyzer show SC": "0.000000",
        "Spectrum analyzer show OUT": "1.000000",
        "Spectrum analyzer pause": "0.000000",
        "Spectrum analyzer signal mode": "0.000000",
        "Spectrum analyzer tilt": "0.000000",
        "Spectrum analyzer speed": "2.000000",
        "Spectrum analyzer show RTMax": "0.000000",
        "Spectrum analyzer show bars": "0.000000",
        "Spectrum analyzer show EQ": "0.000000"
    }

    def __init__(self):
        self.parameters = self.PARAMETERS.copy()

    def create_preset_xml(self, name):
        """Create XML tree for preset"""
        root = ET.Element("PresetXMLTree")
        root.set("version", "1")

        vendor = ET.SubElement(root, "PluginVendor")
        vendor.text = "TBProAudio"

        plugin_name = ET.SubElement(root, "PluginName")
        plugin_name.text = "CS5501V2"

        plugin_version = ET.SubElement(root, "PluginVersion")
        plugin_version.text = "v2.7.2"

        preset = ET.SubElement(root, "Preset")
        preset.set("name", name)

        parameter = ET.SubElement(preset, "Parameter")

        for name, value in self.parameters.items():
            param = ET.SubElement(parameter, "Param")
            param.set("name", name)
            param.set("val", value)

        return root

    def save_preset(self, name, path):
        """Save preset to file"""
        root = self.create_preset_xml(name)
        xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")

        with open(path, "w", encoding="utf-8") as f:
            f.write('<?xml version="1.0" ?>\n')
            f.write(xml_str)


def create_mastering_funk_preset():
    preset = CS5501Parameters()

    # Базовые настройки
    preset.parameters["In Volume L"] = "0.000000"
    preset.parameters["In Volume R"] = "0.000000"
    preset.parameters["Out Volume L"] = "0.000000"
    preset.parameters["Out Volume R"] = "0.000000"

    # Базовая фильтрация
    preset.parameters["Filter0 Off/On"] = "1.000000"
    preset.parameters["Filter0 HP Off/On"] = "1.000000"
    preset.parameters["Filter0 HP F"] = "25.000000"
    preset.parameters["Filter0 HP Slope 6-48dB"] = "3.000000"
    preset.parameters["Filter0 LP Off/On"] = "1.000000"
    preset.parameters["Filter0 LP F"] = "18000.000000"
    preset.parameters["Filter0 LP Slope 6-48dB"] = "1.000000"

    # EQ настройки для подготовки к компрессии
    preset.parameters["Filter0 LF Off/On"] = "1.000000"
    preset.parameters["Filter0 LF Type"] = "1.000000"
    preset.parameters["Filter0 LF F"] = "45.000000"  # Чуть ниже для глубины
    preset.parameters["Filter0 LF G"] = "3.500000"  # Не перегружаем перед компрессией
    preset.parameters["Filter0 LF Q"] = "0.800000"

    # Чистка середины перед компрессией
    preset.parameters["Filter0 LMF Off/On"] = "1.000000"
    preset.parameters["Filter0 LMF F"] = "180.000000"
    preset.parameters["Filter0 LMF G"] = "-2.500000"
    preset.parameters["Filter0 LMF Q"] = "1.400000"

    # Компрессор 0 - Нью-Йоркская параллельная компрессия
    preset.parameters["Comp0 Off/On"] = "1.000000"
    preset.parameters["Comp0 Type"] = "0.000000"  # Classic mode
    preset.parameters["Comp0 Threshold"] = "-25.000000"  # Сильное сжатие
    preset.parameters["Comp0 Ratio"] = "8.000000"  # Агрессивное сжатие
    preset.parameters["Comp0 Attack"] = "5.000000"  # Быстрая атака
    preset.parameters["Comp0 Release"] = "80.000000"  # Музыкальный релиз
    preset.parameters["Comp0 MakeUpGain"] = "6.000000"  # Существенное усиление
    preset.parameters["Comp0 Mix"] = "45.000000"  # Параллельное смешивание

    # Компрессор 1 - Glue компрессия
    preset.parameters["Comp1 Off/On"] = "1.000000"
    preset.parameters["Comp1 Type"] = "0.000000"
    preset.parameters["Comp1 Threshold"] = "-8.000000"
    preset.parameters["Comp1 Ratio"] = "2.500000"
    preset.parameters["Comp1 Attack"] = "15.000000"
    preset.parameters["Comp1 Release"] = "120.000000"
    preset.parameters["Comp1 MakeUpGain"] = "1.500000"
    preset.parameters["Comp1 Mix"] = "100.000000"

    # Многоступенчатая сатурация
    preset.parameters["Saturation Off/On"] = "1.000000"
    preset.parameters["Saturation Mode"] = "1.000000"  # Tube mode
    preset.parameters["Saturation Stages"] = "4.000000"  # Максимум стейджей
    preset.parameters["Saturation Even Harmonics"] = "35.000000"  # Сильные четные гармоники
    preset.parameters["Saturation Odd Harmonics"] = "15.000000"  # Умеренные нечетные
    preset.parameters["Saturation Fluctuation"] = "15.000000"  # Аналоговые флуктуации
    preset.parameters["Saturation Mix"] = "65.000000"  # Существенное влияние

    # Мягкий лимитер для контроля пиков
    preset.parameters["Limit0 Off/On"] = "1.000000"
    preset.parameters["Limit0 Gain"] = "1.000000"
    preset.parameters["Limit0 Release"] = "30.000000"
    preset.parameters["Limit0 Auto release"] = "1.000000"
    preset.parameters["Limit0 Ceiling"] = "-0.300000"

    # После-компрессионный EQ для финального баланса
    preset.parameters["Filter0 MF Off/On"] = "1.000000"
    preset.parameters["Filter0 MF F"] = "2200.000000"
    preset.parameters["Filter0 MF G"] = "2.000000"
    preset.parameters["Filter0 MF Q"] = "0.900000"

    preset.parameters["Filter0 HMF Off/On"] = "1.000000"
    preset.parameters["Filter0 HMF F"] = "5000.000000"
    preset.parameters["Filter0 HMF G"] = "1.800000"
    preset.parameters["Filter0 HMF Q"] = "0.800000"

    preset.parameters["Filter0 HF Off/On"] = "1.000000"
    preset.parameters["Filter0 HF Type"] = "1.000000"
    preset.parameters["Filter0 HF F"] = "11000.000000"
    preset.parameters["Filter0 HF G"] = "2.500000"
    preset.parameters["Filter0 HF Q"] = "0.700000"

    # Аналоговое моделирование для окончательного "склеивания"
    preset.parameters["Analog Off/On"] = "1.000000"

    return preset

def main():
    # Создаем путь к папке с пресетами
    preset_path = pathlib.Path(os.path.expandvars(r"%LOCALAPPDATA%\CS5501V2"))

    # Создаем папку если она не существует
    preset_path.mkdir(parents=True, exist_ok=True)

    # Создаем и сохраняем пресет для мастеринга фонка
    funk_preset = create_mastering_funk_preset()
    funk_preset.save_preset("Mastering Funk", preset_path / "Mastering_Funk.tps")

    print(f"Preset saved to: {preset_path / 'Mastering_Funk.tps'}")


if __name__ == "__main__":
    main()
