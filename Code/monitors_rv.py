from pythonrv import rv
import fileop
import andreil

@rv.monitor(writer = fileop, fd=fileop.f, pd=fileop.path)
@rv.spec(when=rv.PRE, history_size=20)
def open_closed_file(event):
    if (event.called_function.name=="write"):
        if fd.closed():
            fd.open(pd, "w")

@rv.monitor(tok = andreil.Andreil.tokenize, parse=andreil.Andreil.parser, freq = andreil.Andreil.compute_frequency)
@rv.spec(when=rv.POST, history_size=10)
def check_return_size(event):
    assert len(event.fn.tok.result) > 0
    assert len(event.fn.parse.result) > 0
    assert len(event.fn.freq.result) > 0