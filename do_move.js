const fs = require('fs');
try {
    fs.mkdirSync('final_test_dir');
    fs.writeFileSync('final_test_dir/success.txt', 'YES');
} catch (e) {
    fs.writeFileSync('error_log.txt', e.message);
}
