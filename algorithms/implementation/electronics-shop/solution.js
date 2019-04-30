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

// Return  a single integer denoting the amount of money Monica will spend.
// If she doesn't have enough money to buy one keyboard and one USB drive,
// print -1 instead.
function getMoneySpent (keyboards, drives, budget) {
  let total = -1

  for (const keyboard of keyboards) {
    for (const drive of drives) {
      const cost = keyboard + drive

      if (cost <= budget && cost > total) {
        total = cost
      }
    }
  }

  return total
}

function main () {
  const [budget] = readIntegerArray()
  const keyboards = readIntegerArray()
  const drives = readIntegerArray()
  const result = getMoneySpent(keyboards, drives, budget)

  // Open the output stream and write the result.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  ws.write(`${result}\n`)
  ws.end()
}
