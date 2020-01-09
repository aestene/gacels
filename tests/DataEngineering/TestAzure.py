from src.AesLib.DataEngineering import Azure

def testGetSecretFromKeyVault(keyVaultName, secretName):
    secret = Azure.getSecretFromKeyVault(keyVaultName, secretName)
    assert secret == "I'm here for testing purposes!"
