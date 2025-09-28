// Função que recebe uma string como parâmetro
// Contar quantas vezes um caractere se repetiu
class Duplicate {
    constructor(value) {
        this.value = value || 0;
        this.splitValue = [];
        this.repeateds = [];
    }
    readStr() {
        for (let i = 0; i < this.value.length; i++) {
            this.splitValue[i] = this.value[i].toLowerCase();
        }
        this.checkStr();
    }
    checkStr() {
        let isRepeated = false;
        let strArr = this.splitValue;
        for (let index in strArr) {
            index = parseInt(index);
            if (strArr.includes(strArr[index], index + 1)) {
                isRepeated = true;
                if (!this.repeateds.includes(strArr[index])) {
                    this.repeateds.push(strArr[index]);
                }
            }
        }
        this.printResult(isRepeated);
    }
    printResult(status) {
        const correspondences = this.repeateds.length;
        if (status) {
            console.log(`Os valores '${this.repeateds}' se repetem`);
            console.log("Correspondências repetidas => " + correspondences)
        } else {
            console.log("os números não se repetem")
        }
        return correspondences
    }
}

function duplicateCount(test) {
    // let splitValue = [];
    // for (let i = 0; i < test.length; i++) {
    //     for (const letter of test) {
    //         splitValue[i] = test.toLowerCase();
            
    //     }
    //     }      
    if (test == "") {
        return 0;
    }
    new Duplicate(test).readStr()
}
duplicateCount("AbDEA")