def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)


d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}
tds = [generate_tr(name, score) for name, score in d.items()]
print(tds)