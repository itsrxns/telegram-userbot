import subprocess
import command
import module
import util

class SystemModule(module.Module):
    name = 'System'

    @command.desc('Run a snippet in a shell')
    def cmd_shell(self, msg, snip):
        if not snip:
            return '__Provide a snippet to run in shell.__'
        snip = util.filter_input_block(snip)

        self.bot.mresult(msg, 'Running snippet...')
        before = util.time_us()
        try:
            proc = subprocess.run(snip, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
        except subprocess.TimeoutExpired:
            return 'TLE'
        except:
            return 'you messed up!'
        after = util.time_us()

        el_us = after - before
        el_str = f'\nTime: {util.format_duration_us(el_us)}'

        err = f'⚠️ {proc.returncode}' if proc.returncode != 0 else ''
        data = proc.stdout.strip().decode()
        #self.bot.client.send_message(msg.chat.id, "```\n" +data+ "\n```", parse_mode="HTML")

        return f'```{data}```{err}{el_str}'

    @command.desc('Test Internet speed')
    @command.alias('stest')
    def cmd_speedtest(self, msg):
        self.bot.mresult(msg, 'Testing Internet speed, this may take a while...')

        before = util.time_us()
        try:
            proc = subprocess.run(['speedtest'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
        except subprocess.TimeoutExpired:
            return '🕑 `speedtest` took longer than 2 minutes to run.'
        after = util.time_us()

        el_us = after - before
        el_str = f'\nTime: {util.format_duration_us(el_us)}'

        err = f'⚠️ Return code: {proc.returncode}' if proc.returncode != 0 else ''

        out = proc.stdout.strip()
        if proc.returncode == 0:
            lines = out.split('\n')
            out = '\n'.join((lines[4], lines[6], lines[8])) # Server, down, up

        return f'```{out}```{err}{el_str}'
