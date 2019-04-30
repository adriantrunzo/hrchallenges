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

// Return an integer denoting the minimum number of pages Brie must
// turn to get to page p.
// n: the number of pages in the book
function pageCount (n, p) {
  const boundary = Math.ceil(n / 2)
  const leftTargetPage = p % 2 === 0 ? p : p - 1

  if (leftTargetPage < boundary) {
    return leftTargetPage / 2
  } else {
    const leftFinalPage = n % 2 === 0 ? n : n - 1
    return (leftFinalPage - leftTargetPage) / 2
  }
}

function main () {
  const n = Number.parseInt(readLine(), 10)
  const p = Number.parseInt(readLine(), 10)
  const result = pageCount(n, p)

  // Open the output stream and write the result.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  ws.write(`${result}\n`)
  ws.end()
}
