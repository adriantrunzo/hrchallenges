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

// Return the total number of matching pairs of socks that John can sell.
function sockMerchant (socks) {
  const counts = {}
  let pairs = 0

  for (const id of socks) {
    counts[id] = counts[id] ? counts[id] + 1 : 1

    if (counts[id] % 2 === 0) {
      pairs += 1
    }
  }

  return pairs
}

function main () {
  // We don't need to care about the length of the incoming array.
  readLine()

  const socks = readIntegerArray()
  const result = sockMerchant(socks)

  // Open the output stream and write the result.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  ws.write(`${result}\n`)
  ws.end()
}
