class Cipher {
    constructor(shift) {
        this.shift = shift
    }
    encode(str) {
        let newString = "";
        for (let char of str) {
            let i = 0;
            if (!/[A-Za-z]/.test(char)) {
                newString += char
                continue
            }
            char = char.toUpperCase().charCodeAt(0)

            while (i < this.shift) {
                char++
                i++
                if (char > 90 && char < 97 || char > 122) char = 65 
            }
            newString += String.fromCharCode(char)
        }
        return newString
    }
    decode(str) {
        let newString = "";
            for (let char of str) {
                let i = 0;
                if (!/[A-Za-z]/.test(char)) {
                    newString += char
                    continue
                }
                char = char.toUpperCase().charCodeAt(0)

                while (i < this.shift) {
                    char--
                    i++
                    if (char < 65) char = 90
                }
                newString += String.fromCharCode(char)
            }
        return newString
    }      
}

let alg = new Cipher(5)
console.log(alg.encode("Codewars!"))
console.log(alg.decode("HTIJBFWX"))