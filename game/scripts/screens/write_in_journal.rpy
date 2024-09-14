label write_in_journal(tab, entry):
    if tab == "Story":
        $journal_story.append(entry)
    if tab == "People":
        $journal_people.append(entry)
    if tab == "TODO":
        $journal_todo.append(entry)
    $ShowMenu("journal", tab=tab)()
