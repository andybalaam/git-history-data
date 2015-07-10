
from githistorydata.codeline import CodeLine


def expand_authors( log_lines ):
    for log_line in log_lines:
        spl = log_line.author.split( "," )
        weight = 1.0 / len( spl )
        for auth in spl:
            yield CodeLine(
                log_line.commit_hash,
                log_line.date,
                auth.strip(),
                weight
            )
