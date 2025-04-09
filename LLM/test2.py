# test_avalia02.py
import pytest
import torch.nn as nn
from cnn import ConvNet


def test_convnet_eh_classe():
    assert isinstance(ConvNet, type), "ConvNet deve ser uma classe."

def test_convnet_herda_de_nn_module():
    assert issubclass(ConvNet, nn.Module), "ConvNet deve herdar de nn.Module"

def test_convnet_instanciavel():
    try:
        cnn = ConvNet()
        assert True
    except:
        pytest.fail("Não foi possível instanciar ConvNet")

def test_tem_camadas_esperadas():
    cnn = ConvNet()
    for attr in ['conv1', 'pool1', 'conv2', 'drp1', 'pool2', 'lin1']:
        assert hasattr(cnn, attr), f"Atributo '{attr}' ausente em ConvNet"

def test_tipos_das_camadas():
    cnn = ConvNet()
    assert isinstance(cnn.conv1, nn.Conv2d)
    assert isinstance(cnn.pool1, nn.MaxPool2d)
    assert isinstance(cnn.conv2, nn.Conv2d)
    assert isinstance(cnn.drp1, nn.Dropout2d)
    assert isinstance(cnn.pool2, nn.MaxPool2d)
    assert isinstance(cnn.lin1, nn.Linear)

def test_parametros_conv1():
    cnn = ConvNet()
    assert cnn.conv1.in_channels == 1
    assert cnn.conv1.out_channels == 5
    assert cnn.conv1.kernel_size == (6, 6)
    assert cnn.conv1.stride == (2, 2)

def test_parametros_pool1():
    cnn = ConvNet()
    assert cnn.pool1.kernel_size == 2
    assert cnn.pool1.stride == 2

def test_parametros_conv2():
    cnn = ConvNet()
    assert cnn.conv2.in_channels == 5
    assert cnn.conv2.out_channels == 8
    assert cnn.conv2.kernel_size == (3, 3)
    assert cnn.conv2.stride == (1, 1)

def test_dropout():
    cnn = ConvNet()
    assert cnn.drp1.p == 0.25

def test_parametros_pool2():
    cnn = ConvNet()
    assert cnn.pool2.kernel_size == 2

def test_parametros_lin1():
    cnn = ConvNet()
    assert cnn.lin1.in_features == 288  # N12
    assert cnn.lin1.out_features == 10  # N13
