from stegano import exifHeader as stg
from stegano import lsb


img = input("Enter image name(with extension) : ")
# image = Image.open(img, 'r')

s='Major Project Synopsis onHYBRID CRYPTOGRAPHYIn partial fulfillment of requirements for the degree ofBACHELOR OF TECHNOLOGYINCOMPUTER SCIENCE & ENGINEERINGSubmitted by:YAJENDRA PRAJAPATI [19100BTCMCI05568]SANSKAR SINGHAI [19100BTCMCI05554]SAKSHI ROHIDA [19100BTCMCI05551]VIKRAM ABID [19100BTCMCI05567]Under the guidance of Ms. Shweta Jain DEPARTMENT OF COMPUTER SCIENCE & ENGINEERINGSHRI VAISHNAV INSTITUTE OF INFORMATION TECHNOLOGYSHRI VAISHNAV VIDYAPEETH VISHWAVIDYALAYA, INDOREJUL-DEC-2022SHRI VAISHNAV INSTITUTE OF INFORMATION TECHNOLOGYDEPARTMENT OF COMPUTER SCIENCE & ENGINEERINGGUIDELINES FOR MAJOR PROJECT SYNOPSISABSTRACTThe information over internet is becoming a critical issue due to security problems. We have proposed a system for securing the important data from a file i.e., Hybrid Cryptography. Cryptography is a method of protecting information and communications through the use of codes, so that only those for whom the information is intended can read and process it. In this, Cryptography algorithms provides an effective way for protecting sensitive information. It is a method for storing and transmitting data in a form that is only readable by intended users. Over encrypted data, steganography is used to enhanced security. In steganography, the message is to be hidden inside the it enhances confidentially, integrity and security.  Data confidentiality (or privacy): Only an authorized recipient should be able to extract the contents of the message from its encrypted form. Resulting from steps to hide, stop, or delay free access to the encrypted information.Data integrity: The recipient should be able to determine if the message has been altered.Authentication: The recipient should be able to verify from the message, the identity of the sender, the origin or the path it traveled (or combinations) so as to validate claims from emitter or to validated the recipient expectations.Non-repudiation: The remitter should not be able to deny sending the message.7. REFERENCESPutta Bharathi, Gayathri Annam, Jaya Bindu Kandi, Vamsi Krishna Duggana, Anjali T. Secure File Storage using Hybrid Cryptography. DOI: 10.1109/ICCES51350.2021.9489026. Date Added to IEEE Xplore: 02 August 2021.Sherief Murad and Kamel H Rahouma. Hybrid Cryptography for Cloud Security: Methodologies and Designs. DOI:10.1007/978-981-16-2275-57. In book: Digital Transformation Technology (pp.129-140) (January 2022).https://www.geeksforgeeks.org/advanced-encryption-standard-aes/https://www.geeksforgeeks.org/data-encryption-standard-des-set-1/https://www.geeksforgeeks.org/advanced-encryption-standard-aes/ https://www.simplilearn.com/what-is-des-articlehttps://www.geeksforgeeks.org/data-encryption-standard-des-set-1/https://www.geeksforgeeks.org/rc5-encryption-algorithm/#https://towardsdatascience.com/hiding-data-in-an-image-image-steganography-using-python-e491b68b1'

stg.hide(img,"s.jpg",s)
 

print("Done Encode")


Message=stg.reveal("s.jpg")

print(Message)
print()
print(Message.decode('utf-8'))
print("Done decode")



# print(fullText)

# f=open("projectsynopsis.docx","r")


secret = lsb.hide(img,s)
secret.save("s2.png")


clear_message = lsb.reveal("s2.png")
print("Decoded by lsb: -")
print()
print(clear_message)

print()
print(len(s.encode('utf-8')))
