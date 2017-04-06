import logging as l
l.basicConfig(filename="log1.txt",level=l.DEBUG,
format="%(asctime)s->%(levelname)s->%(message)s")
l.info("***********info msg**************")
l.debug('debug msg')
l.warn('warn msg')
l.exception("Exception msg")
l.error("error msg")