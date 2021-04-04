import Settings


class GitSettings(Settings):
    setting_dict
    setting_dict["git_clone_url"] = "https://github.com/zcnmashleu95/duke.git"
    filepath
    repo_directory
    setting_dict["distance_ratio"] = 80

    #assessment_file_paths[10]
    #assessment_file_list
    #report_download_filepath

    # git log
    #include_renames_of_files = False
    #commit_range
    #line_range
    #include_merges = False

    # git blame
    #include_moved_or_copied_lines_in_same_file = False
    #ignore_white_space = False
    #include_moved_or_copied_lines_in_same_commit = False

    def set_settings(self, option, value):
        self.setting_dict[option] = value
        pass

    def get_setting(self, option):
        value = self.setting_dict[option]
        return value