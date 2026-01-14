const { execSync } = require('child_process');
try {
    console.log('Running echo hello...');
    const output = execSync('cmd /c echo hello', { encoding: 'utf8' });
    console.log(output);
    console.log('Success!');
} catch (e) {
    console.error('Failed:', e.stdout || e.message);
    process.exit(1);
}
