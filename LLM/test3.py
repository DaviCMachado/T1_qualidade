# test3.py

from cnn import carregar_modelo_e_dados, evaluate

def test_modelo_trained_accuracy():
    cnn, Xv, Yv = carregar_modelo_e_dados()
    acuracia = evaluate(Xv, Yv, cnn)
    print(f"Acurácia validada: {acuracia:.2f}%")
    assert acuracia > 85.0, f"Acurácia insuficiente: {acuracia:.2f}%"
