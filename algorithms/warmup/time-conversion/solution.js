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

// Returns 24-hour version of given 12-hour time string.
function timeConversion (time) {
  const isPm = (time.slice(-2) === 'PM')
  let [ hours, minutes, seconds ] = time.slice(0, -2).split(':')

  hours = Number.parseInt(hours, 10)

  if (isPm) {
    if (hours < 12) {
      hours += 12
    }
  } else {
    if (hours === 12) {
      hours = 0
    }
  }

  return `${String(hours).padStart(2, '0')}:${minutes}:${seconds}`
}

function main () {
  // Parse the size of the staircase.
  const time = readLine()
  const result = timeConversion(time)

  // Open the output stream.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  ws.write(`${result}\n`)
  ws.end()
}
