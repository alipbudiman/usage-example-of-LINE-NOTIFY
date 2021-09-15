from NotifyFunction import *

alip = LINE_Notify(
    "33TquxG38gVmboJSFKFWelxMarW6AZsp7mGvhng5Qzz" #<< imput your own notify token here
    )

alip.sendMessage("Hello World") #<< send message

alip.sendImage("tmpIMG/FXG (1).png") #<< send image

alip.sendSticker(6325,10979904) #<< send sticker

alip.cekApiStatus( #<< cek Notify api status
    "33TquxG38gVmboJSFKFWelxMarW6AZsp7mGvhng5Qzz"#<< imput your notify token want to cek
    ) 

alip.revokeToken( #<< revoke notify token
    "fEwMDBwFfTYPj5ftsBoblxkxc94tgPEfgYZEVRgPSWp" #<< imput your notify token want to revoke
    )


