const fs = require('fs');
console.log('CWD:', process.cwd());
console.log('Files:', fs.readdirSync('.'));
