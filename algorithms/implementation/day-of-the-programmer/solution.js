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

// Print the full date of Day of the Programmer during the given year in
// the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit
// month, and yyyy is the given year.
function dayOfProgrammer (year) {
  // The 256th day is always in September. In both Julian and Gregorian
  // the 256th day is the 13th on a regular year and the 12th on a
  // leap year. In the 1918 transition year, the first 13 days of February
  // were removed, so the date shifts forward 13 days to the 26th.
  let month = '09'
  let day = '13'

  if (year < 1918) {
    // Julian calendar, leap years are divisble by 4.
    if (year % 4 === 0) {
      day = '12'
    }
  } else if (year === 1918) {
    day = '26'
  } else {
    // Gregorian, leap years are divisble by 400 or by 4 and not 100.
    if (year % 400 === 0 || (year % 4 === 0 && year % 100 !== 0)) {
      day = '12'
    }
  }

  return `${day}.${month}.${year}`
}

function main () {
  // Parse the year.
  const year = Number.parseInt(readLine(), 10)

  const result = dayOfProgrammer(year)

  // Open the output stream and write the result.
  const ws = createWriteStream(process.env.OUTPUT_PATH)

  ws.write(`${result}\n`)
  ws.end()
}
