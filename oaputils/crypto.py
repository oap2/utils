import base64
from Crypto.Cipher import AES


class CryptoAES(object):
    def __init__(self, plain_text: str) -> None:
        """Init CryptoAES class

        Arguments:
            plain_text {str} -- the encrypt and decrypt key's plain text with base64 encode

        Returns:
            None
        """
        self.key = base64.decodebytes(plain_text)
        self.aes = AES.new(self.key, AES.MODE_ECB)

    def add_to_16(self, data) -> str:
        """ Add data length to one or more 16 bytes

        Arguments:
            data {str} -- encrypt data

        Returns:
            str -- one or more 16 bytes data
        """
        while len(data) % 16 != 0:
            data += '\0'
        return data.encode()

    def encrypt(self, data: str) -> str:
        """ encrypt data

        Arguments:
            data {str} -- encrypt data

        Returns:
            str -- encrypted data encode by base64
        """
        encrypted_data = self.aes.encrypt(self.add_to_16(data))
        encrypted_data_base64 = base64.encodebytes(encrypted_data).decode()
        return encrypted_data_base64

    def decrypt(self, data: str) -> str:
        """ decrypt data

        Arguments:
            data {str} -- decrypt data with base64 encode

        Returns:
            str -- decrypt data
        """
        decrypted_data_base64 = base64.decodebytes(data.encode())
        decrypted_data = self.aes.decrypt(decrypted_data_base64).decode().replace('\0', '')
        return decrypted_data
