from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import sys
import ctypes
import resources
import platform

# Imported Ciphers
from ciphers import CaesarCipher
from ciphers import VigenereCipher
from ciphers import ROT13Cipher
from ciphers import PolybiusCipher
from ciphers import AffineCipher
from ciphers import AtbashCipher
from ciphers import HillCipher
from ciphers import ReverseCipher
from ciphers import RailfenceCipher
from ciphers import ColumnarCipher
from ciphers import PlayfairCipher
from ciphers import TwoSquareCipher
from ciphers import BifidCipher
from ciphers import XORCipher
from ciphers import FeistelCipher
from ciphers import DESCipher
from ciphers import FourSquareCipher
from ciphers import ADFGXCipher
from ciphers import ADFGVXCipher

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class UserInterface(QMainWindow):
    def __init__(self):
        super(UserInterface, self).__init__()
        uic.loadUi('main.ui', self)

        self.menu()

        self.setCipher()

        self.ButtonManager()

        self.keyType.setCurrentWidget(self.inputType1)

    def menu(self):
        # Substitution list
        self.subs_list.addItem("Caesar")
        self.subs_list.addItem("ROT 13")
        self.subs_list.addItem("Atbash")
        self.subs_list.addItem("Polybius")
        self.subs_list.addItem("Affine")
        self.subs_list.addItem("Vigenère")
        self.subs_list.addItem("Hill")
        # Transposition list
        self.tran_list.addItem("Reverse Order")
        self.tran_list.addItem("Rail Fence")
        self.tran_list.addItem("Columnar")
        # Combination list
        self.comb_list.addItem("Playfair")
        self.comb_list.addItem("Two Square")
        self.comb_list.addItem("Four Square")
        self.comb_list.addItem("ADFGX")
        self.comb_list.addItem("ADFGVX")
        self.comb_list.addItem("Bifid")
        # Stream list
        self.strm_list.addItem("XOR")
        # Block list
        self.blck_list.addItem("Feistel")
        self.blck_list.addItem("DES")

    def setCipher(self):
        # Substitution
        caesarDesc = "Each letter of a given text is replaced by a letter of some fixed number of positions down the " \
                     "alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on. "
        caesarCond = "Condition: The key must be an integer number i.e. 12 or 23"
        atbashDesc = "The Atbash cipher is a simple substitution cipher, it reverses the alphabet such that each " \
                     "letter is mapped to the letter in the same position in the reverse of the alphabet. For example " \
                     "A beccomes Z, B becomes Y, etc. "
        atbashCond = "Condition: There is no key required for this cipher"

        rotDesc = "ROT13 (rotate 13) is a specific implementation of the Caesar cipher where the shift is always 13 " \
                  "places. "
        rotCond = "Condition: There is no key required for this cipher"
        vigenereDesc = "Vigenere Cipher is a method of encrypting alphabetic text. It uses a simple form of " \
                       "polyalphabetic substitution. A polyalphabetic cipher is any cipher based on substitution, " \
                       "using multiple substitution alphabets .The encryption of the original text is done using the " \
                       "Vigenère square or Vigenère table. "
        vigenereCond = "Condition: The key can be in the form of words or random letters i.e. abc or fire"
        polyDesc = "The Polybius Cipher uses a table called Polybius Square to translate letters into numbers. In " \
                   "order to fit the 26 letters of the alphabet into the 25 spots created by the table, the letters i " \
                   "and j are combined."
        polyCond = "Condition: In the generic type of the square there is no key required"
        affDesc = "The Affine cipher is a type of monoalphabetic substitution cipher, wherein each letter in an " \
                  "alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, " \
                  "and converted back to a letter. In this cipher 26 character of the English alphabet (m = 26) is " \
                  "used.\nEncryption Formula:  E ( x ) = ( a x + b ) mod m\n" \
                  "Decryption Formula: D ( x ) = a^-1 ( x - b ) mod m\n" \
                  "The key consists of two numbers of i.e. a = 11, b = 3. 'a' should be chosen to be relatively prime " \
                  "to m (i.e. a should have no factors in common with m)"
        affCond = "Condition: The a & b 'key' must be entered as a comma separated number. The numbers must be " \
                  "between 0 - 99 i.e. 11,4 or 13, 10"
        hillDesc = "Hill cipher is a polygraphic substitution cipher based on linear algebra.Each letter is " \
                   "represented by a number modulo 26. Often the simple scheme A = 0, B = 1, …, Z = 25 is used, " \
                   "but this is not an essential feature of the cipher. To encrypt a message, each block of n letters " \
                   "(considered as an n-component vector) is multiplied by an invertible n × n matrix, " \
                   "against modulus 26. To decrypt the message, each block is multiplied by the inverse of the matrix " \
                   "used for encryption.\nThe matrix used for encryption is the cipher key, and it should be chosen " \
                   "randomly from the set of invertible n × n matrices (modulo 26). Note: numbers and special " \
                   "characters are replaced and not processed."
        hillCond = "Condition: only a 2x2 matrix as the key is supported & the key[s] must be integer numbers i.e. 1," \
                   "2,3,4 "

        # Transposition
        reverseDesc = "In this cipher the process of encryption and decryption is the same, the order of the " \
                      "message is simply reversed."
        reverseCond = "Condition: There is no key required for this cipher"
        rfenceDesc = "The Rail Fence is a transposition cipher that follows a simple rule for mixing up the " \
                     "characters in the plaintext to form the ciphertext. It works by writing the message on " \
                     "alternate lines (in zigzag pattern) and then read off each of the line in turn. The numeric key " \
                     "in this cipher determines the number of rows (rails) in the zigzag pattern."
        rfenceCond = "Condition: For the cipher to be effective, the key should be in integer number format that is " \
                     "less than the length of the plaintext i.e. 4 or 9 "
        colDesc = "In Columnar Transposition the plaintext is written out in rows, and then the ciphertext is read " \
                  "in columns one by one. Width of the rows and the permutation of the columns are defined by " \
                  "a keyword. If the keyword is of length 4, the length of rows will be 4 as well."
        colCond = "Condition: The key can be either in the form of words, random letters or numbers i.e. fire or 123"

        # Combination
        playDesc = "The Playfair cipher was the first practical digraph substitution cipher. The cipher " \
                   "encrypt/decrypts pairs of letters (digraphs), instead of single letters as in the simple " \
                   "substitution cipher. The playfair cipher consistes of 2 steps. Firstly, the inputted key is " \
                   "converted to a 5×5 square grid of alphabets that acts as the key for encrypting/decrypting the " \
                   "plaintext. And second, the plaintext is split into pairs of two letters (digraphs). If there is " \
                   "an odd number of letters, a Z is added to the last letter.\nNote: between repeated letters in " \
                   "each word and in place of the special characters of the plaintext there is a letter X"
        playCond = "Condition: The key can be in any format i.e. banana or 1apple"
        twoDesc = "The Two-Square cipher, also known as the double Playfair is a polygraphic (multi-diagrpah) " \
                  "substitution cipher. It replaces each plaintext pair of letters by another two letters, based on " \
                  "the two keyword tables. The tables are created based on two given keywords.\nNote: numbers and " \
                  "special characters are not supported."
        twoCond = "Condition: Two keywords are required in order to process the text, double letters/numbers in the " \
                  "key are not valid i.e. orange or street"
        fourDesc = "Similar to Two-Square cipher Four-Square cipher encrypts pairs of letters (diagraphs). The " \
                   "four-square cipher uses four 5 by 5 matrices arranged in a square. Each of the 5 by 5 matrices " \
                   "contains 25 letters, the letter 'j' is merged with 'i'. The four-square algorithm allows for two " \
                   "separate keys, one for each of the two ciphertext matrices.\nNote: numbers and special characters " \
                   "are not supported. "
        fourCond = "Condition: Two keywords are required in order to process the text, double letters/numbers in the " \
                   "'key square' are not valid i.e. orange or sauce"
        adxDesc = "ADFGX is a fractionating transposition cipher which combines a modified Polybius square with a " \
                  "single columnar transposition. The key for this cipher is a 5 by 5 'key square' which contains all " \
                  "the letters of alphabet and the key except the letter 'j'.\nNote:\nKey 1 is for Polybius " \
                  "square.\nKey 2 is for Columnar table.\nNumbers and special characters are not supported. "
        adxCond = "Condition: Two keywords are required in order to process the text, double letters/numbers in the " \
                  "key are not valid i.e. home or flower "
        advxDesc = "ADFGVX is an extended version of ADFGX cipher. The 'key square' in ADFGVX is 6 by 6 which " \
                   "contains the full alphabet and the digits 0 to 9.\nNote:\nKey 1 is for Polybius " \
                   "square.\nKey 2 is for Columnar table.\nSpecial characters are not supported. "
        advxCond = "Condition: Two keywords are required in order to process the text, double letters/numbers in the " \
                   "key are not valid i.e. home or flower"
        bifidDesc = "Bifid is a cipher which combines the Polybius square with transposition, and uses fractionation " \
                    "to achieve diffusion. The key[s] for the Bifid cipher consist of a 25 letter 'key square which " \
                    "contains all the letters of alphabet and the key except the letter 'j'.\nNote: numbers and " \
                    "special characters are removed and not processed."
        bifidCond = "Condition: Double letters/numbers in the key are not valid and are removed i.e. home or flower"

        # Stream
        xorDesc = "XOR cipher is an additive cypher. In XOR operation, the output is true when the inputs differ. XOR " \
                  "operation means “either one but not both or none.” XOR cipher employs the XOR logical operation in " \
                  "order to encrypt data. First, the key's binary value is taken. Then, XOR operation is performed " \
                  "using the key so that an encrypted data is created. Also in order to decrypt, the same key is used " \
                  "with the XOR operation."
        xorCond = "Condition: Since the ASCII table is used in this cipher, the key must be between 0 and less than " \
                  "or equal to 127 i.e. 4 or 85 "

        # Block
        feiDesc = "Feistel Cipher is not a specific scheme of block cipher. It is a design model from which many " \
                  "different block ciphers are derived, in which the same algorithm is used for both encryption and " \
                  "decryption. Encryption/Decryption processes in the Feistel structure consists of multiple rounds " \
                  "of processing of the plaintext, each round consisting of a “substitution” step followed by a " \
                  "permutation step. In here, two rounds of the Feistel structure is used. A key is also used in this " \
                  "cipher, the binary value of which is processed with the binary value of the plaintext in order to " \
                  "generate the ciphertext. "
        feiCond = "Condition: The key must be less than or equal to the length of the plaintext, and it can be in any " \
                  "format i.e. banana or uranium-235 "
        desDesc = "Data Encryption Standard (DES) is a symmetric-key block cipher which is considered as one of the " \
                  "implementations of the Feistel Cipher. It uses 16 rounds of encryption/decryption using a " \
                  "structure similiar to the Feistel model. The block size is 64-bit. The key length is 64-bit, " \
                  "though the cipher only uses 56 bits of it.\nNote: the input for encryption can be in any format, " \
                  "however the input/output for decryption is in Hexadecimal form. "
        desCond = "Condition: The key must be 8 characters long (1 char = 8 bits, 8 x 8 = 64) i.e. academic or horse123"

        self.clear()
        self.keyType.setCurrentWidget(self.inputType1)
        self.subs_key.setEnabled(True)
        self.subs_desc.setText(caesarDesc)
        self.subs_con.setText(caesarCond)

        selected_cipher = self.subs_list.currentText()
        selected_cipher1 = self.tran_list.currentText()
        selected_cipher2 = self.comb_list.currentText()
        selected_cipher3 = self.strm_list.currentText()
        selected_cipher4 = self.blck_list.currentText()
        if selected_cipher == "Vigenère":
            self.clear()
            self.keyType.setCurrentWidget(self.inputType1)
            self.subs_key.setEnabled(True)
            self.subs_desc.setText(vigenereDesc)
            self.subs_con.setText(vigenereCond)
        elif selected_cipher == "ROT 13":
            self.clear()
            self.keyType.setCurrentWidget(self.inputType1)
            self.subs_key.setEnabled(False)
            self.subs_desc.setText(rotDesc)
            self.subs_con.setText(rotCond)
        elif selected_cipher == "Atbash":
            self.clear()
            self.keyType.setCurrentWidget(self.inputType1)
            self.subs_key.setEnabled(False)
            self.subs_desc.setText(atbashDesc)
            self.subs_con.setText(atbashCond)
        elif selected_cipher == "Polybius":
            self.clear()
            self.keyType.setCurrentWidget(self.inputType1)
            self.subs_key.setEnabled(False)
            self.subs_desc.setText(polyDesc)
            self.subs_con.setText(polyCond)
        elif selected_cipher == "Affine":
            self.clear()
            self.keyType.setCurrentWidget(self.inputType1)
            self.subs_key.setEnabled(True)
            self.subs_desc.setText(affDesc)
            self.subs_con.setText(affCond)
        elif selected_cipher == "Hill":
            self.clear()
            self.keyType.setCurrentWidget(self.inputType2)
            self.subs_desc.setText(hillDesc)
            self.subs_con.setText(hillCond)
        # Transposition
        if selected_cipher1 == "Reverse Order":
            self.clear()
            self.tran_key.setEnabled(False)
            self.tran_desc.setText(reverseDesc)
            self.tran_con.setText(reverseCond)
        elif selected_cipher1 == "Rail Fence":
            self.clear()
            self.tran_key.setEnabled(True)
            self.tran_desc.setText(rfenceDesc)
            self.tran_con.setText(rfenceCond)
        elif selected_cipher1 == "Columnar":
            self.clear()
            self.tran_key.setEnabled(True)
            self.tran_desc.setText(colDesc)
            self.tran_con.setText(colCond)
        # Combination
        if selected_cipher2 == "Playfair":
            self.clear()
            self.keyType_2.setCurrentWidget(self.inpType1)
            self.comb_desc.setText(playDesc)
            self.comb_con.setText(playCond)
        elif selected_cipher2 == "Two Square":
            self.clear()
            self.keyType_2.setCurrentWidget(self.inpType2)
            self.comb_desc.setText(twoDesc)
            self.comb_con.setText(twoCond)
        elif selected_cipher2 == "Four Square":
            self.clear()
            self.keyType_2.setCurrentWidget(self.inpType2)
            self.comb_desc.setText(fourDesc)
            self.comb_con.setText(fourCond)
        elif selected_cipher2 == "ADFGX":
            self.clear()
            self.keyType_2.setCurrentWidget(self.inpType2)
            self.comb_desc.setText(adxDesc)
            self.comb_con.setText(adxCond)
        elif selected_cipher2 == "ADFGVX":
            self.clear()
            self.keyType_2.setCurrentWidget(self.inpType2)
            self.comb_desc.setText(advxDesc)
            self.comb_con.setText(advxCond)
        elif selected_cipher2 == "Bifid":
            self.clear()
            self.keyType_2.setCurrentWidget(self.inpType1)
            self.comb_desc.setText(bifidDesc)
            self.comb_con.setText(bifidCond)
        # Stream
        if selected_cipher3 == "XOR":
            self.clear()
            self.strm_desc.setText(xorDesc)
            self.strm_con.setText(xorCond)
        # Block
        if selected_cipher4 == "Feistel":
            self.clear()
            self.blck_desc.setText(feiDesc)
            self.blck_con.setText(feiCond)
        elif selected_cipher4 == "DES":
            self.clear()
            self.blck_desc.setText(desDesc)
            self.blck_con.setText(desCond)

    def clear(self):
        # Substitution
        self.subs_pt.clear()
        self.subs_ct.clear()
        self.subs_key.clear()
        self.h_key1.clear()
        self.h_key2.clear()
        self.h_key3.clear()
        self.h_key4.clear()
        # Transposition
        self.tran_pt.clear()
        self.tran_ct.clear()
        self.tran_key.clear()
        # Combination
        self.comb_pt.clear()
        self.comb_ct.clear()
        self.comb_key.clear()
        self.comb_keyw1.clear()
        self.comb_keyw2.clear()
        # Stream
        self.strm_pt.clear()
        self.strm_ct.clear()
        self.strm_key.clear()
        # Block
        self.blck_pt.clear()
        self.blck_ct.clear()
        self.blck_key.clear()

    def subsCipherRun(self):
        try:
            if self.subs_list.currentText() == "Caesar":
                if self.subs_ct.toPlainText() == "":
                    self.subs_ct.setPlainText(
                        CaesarCipher.encrypt(self.subs_pt.toPlainText(), int(self.subs_key.text())))
                else:
                    self.subs_pt.setPlainText(
                        CaesarCipher.decrypt(self.subs_ct.toPlainText(), int(self.subs_key.text())))
            elif self.subs_list.currentText() == "ROT 13":
                if self.subs_ct.toPlainText() == "":
                    self.subs_ct.setPlainText(ROT13Cipher.encrypt(self.subs_pt.toPlainText()))
                else:
                    self.subs_pt.setPlainText(ROT13Cipher.decrypt(self.subs_ct.toPlainText()))
            elif self.subs_list.currentText() == "Atbash":
                if self.subs_ct.toPlainText() == "":
                    self.subs_ct.setPlainText(AtbashCipher.atbash(self.subs_pt.toPlainText()))
                else:
                    self.subs_pt.setPlainText(AtbashCipher.atbash(self.subs_ct.toPlainText()))
            elif self.subs_list.currentText() == "Polybius":
                if self.subs_ct.toPlainText() == "":
                    self.subs_ct.setPlainText(PolybiusCipher.encrypt(self.subs_pt.toPlainText()))
                else:
                    self.subs_pt.setPlainText(PolybiusCipher.decrypt(self.subs_ct.toPlainText()))
            elif self.subs_list.currentText() == "Vigenère":
                if self.subs_ct.toPlainText() == "":
                    self.subs_ct.setPlainText(VigenereCipher.encrypt(self.subs_pt.toPlainText(), self.subs_key.text()))
                else:
                    self.subs_pt.setPlainText(VigenereCipher.decrypt(self.subs_ct.toPlainText(), self.subs_key.text()))
            elif self.subs_list.currentText() == "Affine":
                if self.subs_ct.toPlainText() == "":
                    self.subs_ct.setPlainText(AffineCipher.encrypt(self.subs_pt.toPlainText(), self.subs_key.text()))
                else:
                    self.subs_pt.setPlainText(AffineCipher.decrypt(self.subs_ct.toPlainText(), self.subs_key.text()))
            elif self.subs_list.currentText() == "Hill":
                if self.subs_ct.toPlainText() == "":
                    self.subs_ct.setPlainText(
                        HillCipher.encrypt(self.subs_pt.toPlainText(), self.h_key1.text(), self.h_key2.text(),
                                           self.h_key3.text(), self.h_key4.text()))
                else:
                    self.subs_pt.setPlainText(
                        HillCipher.decrypt(self.subs_ct.toPlainText(), self.h_key1.text(), self.h_key2.text(),
                                           self.h_key3.text(), self.h_key4.text()))
        except ValueError:
            ctypes.windll.user32.MessageBoxW(None, "No data entered/Invalid Key", "Error!", 0)

    def tranCipherRun(self):
        try:
            if self.tran_list.currentText() == "Reverse Order":
                if self.tran_ct.toPlainText() == "":
                    self.tran_ct.setPlainText(ReverseCipher.reverse(self.tran_pt.toPlainText()))
                else:
                    self.tran_pt.setPlainText(ReverseCipher.reverse(self.tran_ct.toPlainText()))
            elif self.tran_list.currentText() == "Rail Fence":
                if self.tran_ct.toPlainText() == "":
                    self.tran_ct.setPlainText(RailfenceCipher.encrypt(self.tran_pt.toPlainText(), self.tran_key.text()))
                else:
                    self.tran_pt.setPlainText(RailfenceCipher.decrypt(self.tran_ct.toPlainText(), self.tran_key.text()))
            elif self.tran_list.currentText() == "Columnar":
                if self.tran_ct.toPlainText() == "":
                    self.tran_ct.setPlainText(ColumnarCipher.encrypt(self.tran_pt.toPlainText(), self.tran_key.text()))
                else:
                    self.tran_pt.setPlainText(ColumnarCipher.decrypt(self.tran_ct.toPlainText(), self.tran_key.text()))

        except ValueError:
            ctypes.windll.user32.MessageBoxW(None, "No data entered/Invalid Key", "Error!", 0)

    def combCipherRun(self):
        try:
            if self.comb_list.currentText() == "Playfair":
                if self.comb_ct.toPlainText() == "":
                    self.comb_ct.setPlainText(PlayfairCipher.encrypt(self.comb_pt.toPlainText(), self.comb_key.text()))
                else:
                    self.comb_pt.setPlainText(PlayfairCipher.decrypt(self.comb_ct.toPlainText(), self.comb_key.text()))
            elif self.comb_list.currentText() == "Two Square":
                if self.comb_ct.toPlainText() == "":
                    self.comb_ct.setPlainText(
                        TwoSquareCipher.encrypt(self.comb_pt.toPlainText(), self.comb_keyw1.text(),
                                                self.comb_keyw2.text()))
                else:
                    self.comb_pt.setPlainText(
                        TwoSquareCipher.decrypt(self.comb_ct.toPlainText(), self.comb_keyw1.text(),
                                                self.comb_keyw2.text()))
            elif self.comb_list.currentText() == "Four Square":
                if self.comb_ct.toPlainText() == "":
                    self.comb_ct.setPlainText(
                        FourSquareCipher.encrypt(self.comb_pt.toPlainText(), self.comb_keyw1.text(),
                                                 self.comb_keyw2.text()))
                else:
                    self.comb_pt.setPlainText(
                        FourSquareCipher.decrypt(self.comb_ct.toPlainText(), self.comb_keyw1.text(),
                                                 self.comb_keyw2.text()))
            elif self.comb_list.currentText() == "ADFGX":
                if self.comb_ct.toPlainText() == "":
                    self.comb_ct.setPlainText(ADFGXCipher.encrypt(self.comb_pt.toPlainText(), self.comb_keyw1.text(),
                                                                  self.comb_keyw2.text()))
                else:
                    self.comb_pt.setPlainText(ADFGXCipher.decrypt(self.comb_ct.toPlainText(), self.comb_keyw1.text(),
                                                                  self.comb_keyw2.text()))
            elif self.comb_list.currentText() == "ADFGVX":
                if self.comb_ct.toPlainText() == "":
                    self.comb_ct.setPlainText(ADFGVXCipher.encrypt(self.comb_pt.toPlainText(), self.comb_keyw1.text(),
                                                                   self.comb_keyw2.text()))
                else:
                    self.comb_pt.setPlainText(ADFGVXCipher.decrypt(self.comb_ct.toPlainText(), self.comb_keyw1.text(),
                                                                   self.comb_keyw2.text()))
            elif self.comb_list.currentText() == "Bifid":
                if self.comb_ct.toPlainText() == "":
                    self.comb_ct.setPlainText(BifidCipher.encrypt(self.comb_pt.toPlainText(), self.comb_key.text()))
                else:
                    self.comb_pt.setPlainText(BifidCipher.decrypt(self.comb_ct.toPlainText(), self.comb_key.text()))

        except ValueError:
            ctypes.windll.user32.MessageBoxW(None, "No data entered/Invalid Key", "Error!", 0)

    def strmCipherRun(self):
        try:
            if self.strm_list.currentText() == "XOR":
                if self.strm_ct.toPlainText() == "":
                    self.strm_ct.setPlainText(XORCipher.xor(self.strm_pt.toPlainText(), self.strm_key.text()))
                else:
                    self.strm_pt.setPlainText(XORCipher.xor(self.strm_ct.toPlainText(), self.strm_key.text()))
        except ValueError:
            ctypes.windll.user32.MessageBoxW(None, "No data entered/Invalid Key", "Error!", 0)

    def blckCipherRun(self):
        try:
            if self.blck_list.currentText() == "Feistel":
                if self.blck_ct.toPlainText() == "":
                    self.blck_ct.setPlainText(FeistelCipher.encrypt(self.blck_pt.toPlainText(), self.blck_key.text()))
                else:
                    self.blck_pt.setPlainText(FeistelCipher.decrypt(self.blck_ct.toPlainText(), self.blck_key.text()))
            elif self.blck_list.currentText() == "DES":
                if self.blck_ct.toPlainText() == "":
                    self.blck_ct.setPlainText(
                        DESCipher.DESCipher(self.blck_pt.toPlainText(), self.blck_key.text(), "enc"))
                else:
                    self.blck_pt.setPlainText(
                        DESCipher.DESCipher(self.blck_ct.toPlainText(), self.blck_key.text(), "dec"))
        except ValueError:
            ctypes.windll.user32.MessageBoxW(None, "No data entered/Invalid Key", "Error!", 0)

    def ButtonManager(self):
        self.subs_list.currentTextChanged.connect(self.setCipher)
        self.tran_list.currentTextChanged.connect(self.setCipher)
        self.comb_list.currentTextChanged.connect(self.setCipher)
        self.strm_list.currentTextChanged.connect(self.setCipher)
        self.blck_list.currentTextChanged.connect(self.setCipher)
        self.subs_btn.clicked.connect(self.subsCipherRun)
        self.tran_btn.clicked.connect(self.tranCipherRun)
        self.comb_btn.clicked.connect(self.combCipherRun)
        self.strm_btn.clicked.connect(self.strmCipherRun)
        self.blck_btn.clicked.connect(self.blckCipherRun)
        self.uni_clr.clicked.connect(self.clear)
        self.uni_clr_2.clicked.connect(self.clear)
        self.uni_clr_3.clicked.connect(self.clear)
        self.uni_clr_4.clicked.connect(self.clear)
        self.uni_clr_5.clicked.connect(self.clear)


app = QApplication(sys.argv)
user_interface = UserInterface()

app.exec()
