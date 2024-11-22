# %%
text = """
Branch#
branch_icon: string - the icon to use in front of the git branch name - defaults to \uE0A0
branch_identical_icon: string - the icon to display when remote and local are identical - defaults to \u2261
branch_ahead_icon: string - the icon to display when the local branch is ahead of its remote - defaults to \u2191
branch_behind_icon: string - the icon to display when the local branch is behind its remote - defaults to \u2193
branch_gone_icon: string - the icon to display when there's no remote branch - defaults to \u2262
branch_max_length: int - the max length for the displayed branch name where 0 implies full length - defaults to 0
HEAD#
commit_icon: string - icon/text to display before the commit context (detached HEAD) - defaults to \uF417
tag_icon: string - icon/text to display before the tag context - defaults to \uF412
rebase_icon: string - icon/text to display before the context when in a rebase - defaults to \uE728
cherry_pick_icon: string - icon/text to display before the context when doing a cherry-pick - defaults to \uE29B
revert_icon: string - icon/text to display before the context when doing a revert - defaults to \uF0E2
merge_icon: string icon/text to display before the merge context - defaults to \uE727
no_commits_icon: string icon/text to display when there are no commits in the repo - defaults to \uF594
Upstream#
github_icon: string - icon/text to display when the upstream is Github - defaults to \uF408
gitlab_icon: string - icon/text to display when the upstream is Gitlab - defaults to \uF296
bitbucket_icon: string - icon/text to display when the upstream is Bitbucket - defaults to \uF171
azure_devops_icon: string - icon/text to display when the upstream is Azure DevOps - defaults to \uFD03
git_icon: string - icon/text to display when the upstream is not known/mapped - defaults to \uE5FB
"""

print(text)
