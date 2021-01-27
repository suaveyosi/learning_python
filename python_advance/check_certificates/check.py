import ssl, socket, OpenSSL

hostname = 'google.com'
ctx = ssl.create_default_context()
s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
#s.connect((hostname, 443))
s.connect(('google.com',443))
cert = s.getpeercert()

subject = dict(x[0] for x in cert['subject'])
issued_to = subject['commonName']
issuer = dict(x[0] for x in cert['issuer'])
issued_by = issuer['commonName']

print(issued_to)
print(issued_by)

#def getCertificate(s):
#
#        cert_pem = ssl.get_server_certificate((s, 443))
#        cert_der = ssl.PEM_cert_to_DER_cert(cert_pem)
#        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert_pem)
#
#        fingerprint = x509.digest('sha1')
#        fingerprint = ':'.join(fingerprint[pos:pos+2] for pos in xrange(0,len(fingerprint),2))
#        subject = x509.get_subject()
#
#        print('%-25s %s' %('SHA1 Fingerprint:',fingerprint))
#        print('%-25s %s' %('Serial Number:',x509.get_serial_number()))
#        print('%-25s %s' %('Common Name:',subject.CN))
#        print('%-25s %s' %('Organization:',subject.O))
#        print('%-25s %s' %('Issue Date:',x509.get_notBefore()))
#        print('%-25s %s' %('Expiration Date:', x509.get_notAfter()))
#
#        cert_out = open(s,'wb')
#        cert_out.write(cert_pem)
#        cert_out.close() 
#
#getCertificate('google.com')