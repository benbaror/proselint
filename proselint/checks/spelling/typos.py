# -*- coding: utf-8 -*-
"""Misspellings.

---
layout:     post
source:
source_url:
title:      typos
date:
categories: writing
---

Points out typos.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "spelling.typos"
    msg = "Probably meant '{}'."

    misspellings = [
        ["still",          ["stile"]],
    ]

    return preferred_forms_check(text, misspellings, err, msg)
