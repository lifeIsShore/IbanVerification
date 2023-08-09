

<body>
<h1>IBAN Verification</h1>
<p>This Python script verifies the validity of an IBAN (International Bank Account Number) according to the IBAN structure and checksum rules. It calculates the check digits and validates the IBAN using the mod-97 algorithm.</p>

<h2>How It Works</h2>
<p>1. The script extracts the first two letters from the IBAN, converts them to numbers using their positions in the alphabet (A=10, B=11, etc.), and uses these numbers to calculate the check digits.
    2. The country code, check digit, bank code, and account number are extracted from the IBAN.
    3. The IBAN part for validation is constructed by combining the bank code, account number, and calculated check digits.
    4. The mod-97 operation is performed on the constructed IBAN part, and the result is subtracted from 98 to calculate the IBAN mod value.
    5. The calculated mod value is compared with the provided check digit to determine the validity of the IBAN.</p>

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
