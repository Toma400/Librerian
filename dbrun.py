diction = {
    "a": "aaa",
    "b": "555"
}

from core.technical.repo_manag import js_create, js_read, js_change
js_create("accounts/", "test", diction)
js_change("accounts/test.json", "a", "abc")
b = js_read("accounts/test.json", "b"); print (b)