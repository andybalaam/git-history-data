
from githistorydata.codeline import CodeLine
from githistorydata.dataline import DataLine


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


def expand_detail( commit_detail, weight ):
    return (
        DataLine(
            commit_detail.commit_hash,
            commit_detail.date,
            commit_detail.author,
            int( fc.added   * weight ),
            int( fc.removed * weight ),
            fc.name
        )
        for fc in commit_detail.file_changes
    )


def expand_lines( git, code_lines ):
    for ln in code_lines:
        commit_detail = git.show( ln.commit_hash, ln.date, ln.author )
        for data_line in expand_detail( commit_detail, ln.weight ):
            yield data_line
