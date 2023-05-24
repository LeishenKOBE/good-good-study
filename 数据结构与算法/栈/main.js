class Stack {
    constructor() {
        this.items = []
    }
    push(i) {
        this.items.push(i)
    }
}

const s = new Stack()
s.items.push(1)
console.log(s.items)