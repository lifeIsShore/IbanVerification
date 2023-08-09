

<body>
<h1>IBAN Verification</h1>
<p>This Python script verifies the validity of an IBAN (International Bank Account Number) according to the IBAN structure and checksum rules. It calculates the check digits and validates the IBAN using the mod-97 algorithm.</p>

<h2>How It Works</h2>
<p>1. The script extracts the first two letters from the IBAN, converts them to numbers using their positions in the alphabet (A=10, B=11, etc.), and uses these numbers to calculate the check digits.</p>
<p> 2. The country code, check digit, bank code, and account number are extracted from the IBAN.</p>
<p>3. The IBAN part for validation is constructed by combining the bank code, account number, and calculated check digits.</p>
<p>  4. The mod-97 operation is performed on the constructed IBAN part, and the result is subtracted from 98 to calculate the IBAN mod value.</p>
<p> 5. The calculated mod value is compared with the provided check digit to determine the validity of the IBAN.</p>

<h2>Usage</h2>
<p>You can use the <code>iban_verification()</code> function to verify an IBAN. Provide the complete IBAN as an argument, and the function will return <code>True</code> if the IBAN is valid and <code>False</code> if it's not.</p>

<h3>Example:</h3>
<pre><code>is_valid = iban_verification("DE29100100100987654324")
print(is_valid)  // Output: False</code></pre>

<h2>Contributing</h2>
<p>This project is open source, and contributions are welcome. Feel free to submit pull requests for improvements or bug fixes.</p>

<h2>License</h2>
<p>This project is licensed under the <a href="LICENSE">MIT License</a>. For more information, please refer to the license file.</p>
</body>







<body>
<h1>IBAN-Verifizierung</h1>
<p>Dieses Python-Skript überprüft die Gültigkeit einer IBAN (Internationale Bankkontonummer) gemäß der IBAN-Struktur und Prüfziffernregeln. Es berechnet die Prüfziffern und verifiziert die IBAN mithilfe des Modulo-97-Algorithmus.</p>

<h2>Funktionsweise</h2>
<p>1. Das Skript extrahiert die ersten beiden Buchstaben aus der IBAN, wandelt sie in Zahlen um, indem ihre Positionen im Alphabet verwendet werden (A=10, B=11 usw.), und verwendet diese Zahlen, um die Prüfziffern zu berechnen.<p>
<p>2. Der Ländercode, die Prüfziffer, die Bankleitzahl und die Kontonummer werden aus der IBAN extrahiert.<p>
<p>3. Der IBAN-Teil für die Verifizierung wird konstruiert, indem die Bankleitzahl, die Kontonummer und die berechneten Prüfziffern kombiniert werden.<p>
<p>4. Die Modulo-97-Operation wird auf dem konstruierten IBAN-Teil durchgeführt, und das Ergebnis wird von 98 subtrahiert, um den IBAN-Modulo-Wert zu berechnen.<p>
<p>5. Der berechnete Modulo-Wert wird mit der angegebenen Prüfziffer verglichen, um die Gültigkeit der IBAN festzustellen.</p>

<h2>Verwendung</h2>
<p>Sie können die Funktion <code>iban_verification()</code> verwenden, um eine IBAN zu überprüfen. Geben Sie die vollständige IBAN als Argument an, und die Funktion gibt <code>True</code> zurück, wenn die IBAN gültig ist, andernfalls gibt sie <code>False</code> zurück.</p>

<h3>Beispiel:</h3>
<pre><code>is_valid = iban_verification("DE29100100100987654324")
print(is_valid)  // Ausgabe: False</code></pre>

<h2>Mitwirken</h2>
<p>Dieses Projekt ist Open Source, und Beiträge sind willkommen. Sie können gerne Pull Requests für Verbesserungen oder Fehlerkorrekturen einreichen.</p>

<h2>Lizenz</h2>
<p>Dieses Projekt ist unter der <a href="LICENSE">MIT-Lizenz</a> lizenziert. Weitere Informationen finden Sie in der Lizenzdatei.</p>
</body>


