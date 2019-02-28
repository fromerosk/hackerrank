function validateIP(ip) {
	/**
	@param ip: string
	@return: boolean
	*/

    // your code goes here
    let bytes = ip.split('.');
    //   console.log(bytes);
    //   console.log(bytes.length);
    if (bytes.length != 4) {
        return false;
    }

    for (let i = 0; i < 4; i++) {
        if (!/^\d*$/.test(bytes[i])){
            return false;
        }
        let numb = parseInt(bytKUSes[i], 10);
        if (isNaN(numb) || numb > 255 || numb < 0) {
            return false;
        }
    }

    return true;
}


console.log(validateIP("1.2.3.0x1"));