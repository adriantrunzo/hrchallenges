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

// Compare the given triplets
function compareTriplets (a, b) {
  let scoreA = 0
  let scoreB = 0

  for (let i = 0; i < a.length; i++) {
    if (a[i] > b[i]) {
      scoreA += 1
    } else if (b[i] > a[i]) {
      scoreB += 1
    }
  }

  return [scoreA, scoreB]
}

function main () {
  // Parse the two input triplets and compare.
  const first = readLine().split(' ').map(v => Number.parseInt(v, 10))
  const second = readLine().split(' ').map(v => Number.parseInt(v, 10))
  const result = compareTriplets(first, second)

  // Open the output stream and write the result.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  ws.write(`${result.join(' ')}\n`)
  ws.end()
}
