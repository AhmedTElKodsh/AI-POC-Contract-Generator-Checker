console.log('Hello from Node');
const fs = require('fs');
if (!fs.existsSync('test_dir_node')) {
    fs.mkdirSync('test_dir_node');
    console.log('Dir created');
}
