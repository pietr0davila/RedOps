// Classe que detecta duplicados
class Duplicate {
    constructor(value) {
        this.value = value || "";
        this.splitValue = [];
        this.repeateds = [];
    }

    readStr() {
        for (let i = 0; i < this.value.length; i++) {
            this.splitValue[i] = this.value[i].toLowerCase();
        }
        return this.checkStr(); // <-- precisa retornar o resultado
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
        return this.printResult(isRepeated); // <-- retorna o número de correspondências
    }

    printResult(status) {
        const correspondences = this.repeateds.length;
        if (status) {
            console.log(`Os valores ${this.repeateds} se repetem`);
            console.log("Correspondências repetidas => " + correspondences)
        } else {
            console.log("os números não se repetem")
        }
        return correspondences;
    }
}

// Função wrapper
function duplicateCount(test) {
    if (test === "") {
        return 0;
    }
    return new Duplicate(test).readStr();
}

