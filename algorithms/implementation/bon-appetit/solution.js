'use strict'

const { createWriteStream } = require('fs')

// Swtich stdin into flowing mode.
process.stdin.resume()
process.stdin.setEncoding('utf-8')

let input = ''
let inputIndex = 0

// Add incoming data to the input buffer.
process.stdin.on('data', chunk => {
  input += chunk
})

// When there is no more input to be read, split it into an array
// and call main().
process.stdin.on('end', () => {
  input = input.trim().split('\n').map(s => s.trim())
  main()
})

// Helper method to read the next input line from the buffer.
function readLine () {
  return input[inputIndex++]
}

function readIntegerArray () {
  return readLine().split(' ').map(v => Number.parseInt(v, 10))
}

// If Brian did not overcharge Anna, return 'Bon Appetit';
// otherwise, return the difference that Brian must refund to Anna.
// This will always be an integer.
// bill: an array of integers representing the cost of each item ordered
// k: an integer representing the index of the item Anna doesn't eat
// b: the amount of money that Anna contributed to the bill
function bonAppetit (bill, k, b) {
  let total = 0

  for (let i = 0; i < bill.length; i++) {
    if (i !== k) {
      total += bill[i]
    }
  }

  const target = total / 2
  return b === target ? 'Bon Appetit' : b - target
}

function main () {
  const [, k] = readIntegerArray()
  const bill = readIntegerArray()
  const b = Number.parseInt(readLine(), 10)

  const result = bonAppetit(bill, k, b)

  // Open the output stream and write the result.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  ws.write(`${result}\n`)
  ws.end()
}
