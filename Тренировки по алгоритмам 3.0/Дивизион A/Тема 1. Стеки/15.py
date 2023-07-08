alphabet = ['<', '>', '/']
for char in range(ord('a'), ord('z') + 1):
    alphabet.append(chr(char))


def read_input():
    return input()


def to_tags(xml):
    if xml[0] != '<' or xml[-1] != '>':
        return None
    size = len(xml)
    tags = []
    i, j = 0, 0
    while i < size and j < size:
        if xml[i] != '<':
            return None
        j = i + 1
        while i < size and xml[j] != '>':
            if xml[j] == '<':
                return None
            j += 1
        tags.append(xml[i + 1:j])
        i = j + 1
    return tags


def check_xml(tags):
    if tags is None:
        return False
    stack = []
    try:
        for tag in tags:
            if tag[0] != '/':
                stack.append(tag)
                continue
            if not len(stack):
                return False
            popped = stack.pop()
            if tag[1:] != popped:
                return False
    except:
        return False
    if len(stack):
        return False
    return True


def restore(xml):
    for i, c in enumerate(xml):
        for char_to_replace in alphabet:
            modified_xml = xml[0:i] + char_to_replace + xml[i + 1:]
            if check_xml(to_tags(modified_xml)):
                return modified_xml


assert (restore('<a></b>') == '<b></b>' or restore('<a></b>') == '<a></a>')
assert restore('<a><aa>') == '<a></a>'
assert restore('<a><>a>') == '<a></a>'
assert restore('<a/</a>') == '<a></a>'
assert restore('<a><ab></ab><cc</c></a>') == '<a><ab></ab><c></c></a>'

assert check_xml(['a', '/a'])
assert not check_xml(['a', '/b'])
assert not check_xml(['a', 'a'])
assert not check_xml(['a', 'b', '/a', '/b'])
assert check_xml(['a', 'b', '/b', '/a'])
assert not check_xml(['a'])

assert not check_xml(to_tags('<a><ab></ab><cc</c></a>'))
assert check_xml(to_tags('<a><ab></ab><c></c></a>'))
assert restore(
    '<fjsm><mb><wvs><zwcac></zwcac><pz></pz></wvs><e><ai></ai><iiilx></iiilx><fnko></fnko></e><zjam></zjam></mb><lh><c></c><m></m></lh><kbbbl><mnb><gx><d><vnyto></vnyto></d><tc></tc><lobb></lobb><krj></krj><ci></ci></gx><hptid><rjc></rjc><jw><wvck></wvck></jw><sheyv></sheyv><zl></zl></hptid><wy></wy><lczx><q></q></lczx><ok></ok></mnb><a></a><sw></sw><r></r></kbbbl><fjrn><ixnq><x><deoft></deoft><mhe></mhe><ols></ols></x><od></od><hlfo></hlfo></ixnq><b></b><l></l></fjrn><yezfq></yezfq><thwc><a><ulbk></ulbk></a><z></z></thwc><ddgmm></ddgmm></fjsm><f><gvvm></gvvm><zsnfd></zsnfd></f><bkjhs><epr></epr></bkjhs><hzu></hzu><grnn><q><m></m><t><mtg></mtg></t><ew></e<></q><ojeoh></ojeoh></grnn><hwbc></hwbc><xlgf></xlgf>') \
    == '<fjsm><mb><wvs><zwcac></zwcac><pz></pz></wvs><e><ai></ai><iiilx></iiilx><fnko></fnko></e><zjam></zjam></mb><lh><c></c><m></m></lh><kbbbl><mnb><gx><d><vnyto></vnyto></d><tc></tc><lobb></lobb><krj></krj><ci></ci></gx><hptid><rjc></rjc><jw><wvck></wvck></jw><sheyv></sheyv><zl></zl></hptid><wy></wy><lczx><q></q></lczx><ok></ok></mnb><a></a><sw></sw><r></r></kbbbl><fjrn><ixnq><x><deoft></deoft><mhe></mhe><ols></ols></x><od></od><hlfo></hlfo></ixnq><b></b><l></l></fjrn><yezfq></yezfq><thwc><a><ulbk></ulbk></a><z></z></thwc><ddgmm></ddgmm></fjsm><f><gvvm></gvvm><zsnfd></zsnfd></f><bkjhs><epr></epr></bkjhs><hzu></hzu><grnn><q><m></m><t><mtg></mtg></t><ew></ew></q><ojeoh></ojeoh></grnn><hwbc></hwbc><xlgf></xlgf>'


def main():
    print(restore(read_input()))


if __name__ == '__main__':
    main()
