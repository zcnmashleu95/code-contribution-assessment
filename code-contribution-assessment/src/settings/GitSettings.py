import Settings


class GitSettings(Settings):
    git_clone_url
    repo_directory
    assessment_file_paths[10]
    assessment_file_list
    report_download_filepath

    # git log
    include_renames_of_files = False
    commit_range
    line_range
    include_merges = False

    # git blame
    include_moved_or_copied_lines_in_same_file = False
    ignore_white_space = False
    include_moved_or_copied_lines_in_same_commit = False
