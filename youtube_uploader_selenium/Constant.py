class Constant:
    """A class for storing constants for YoutubeUploader class"""
    YOUTUBE_URL = 'https://www.youtube.com/'# 'https://www.youtube.com'
    YOUTUBE_STUDIO_URL = 'https://studio.youtube.com'
    YOUTUBE_UPLOAD_URL = 'https://www.youtube.com/upload'
    
    USER_WAITING_TIME = 1

    DESCRIPTION_CONTAINER = '//body/ytcp-uploads-dialog[1]/tp-yt-paper-dialog[1]/div[1]/ytcp-animatable[1]/ytcp-video-metadata-editor[1]/div[1]/ytcp-video-metadata-editor-basics[1]/div[2]/ytcp-mention-textbox[1]/ytcp-form-input-container[1]/div[1]/div[2]'
    
    TAGS_PATH = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[3]/ytcp-form-input-container/div[1]/div[2]/ytcp-free-text-chip-bar/ytcp-chip-bar/div'
    
    KIDS_NOT_PATH = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]/div[2]/ytcp-ve'
    
    TEXTBOX = '//*[@id="textbox"]'
    TEXT_INPUT = 'text-input'
    RADIO_LABEL = 'radioLabel'
    STATUS_CONTAINER = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/' \
                       'div/div[1]/ytcp-video-upload-progress/span'
    NOT_MADE_FOR_KIDS_LABEL = 'NOT_MADE_FOR_KIDS'

    MORE_BUTTON = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/div/ytcp-button'
    TAGS_INPUT_CONTAINER = '//*[@id="text-input"]'
    TAGS_INPUT = 'text-input'
    NEXT_BUTTON = 'next-button'
    VIDEO_URL_CONTAINER = "//span[@class='video-url-fadeable style-scope ytcp-video-info']"
    VIDEO_URL_ELEMENT = "//a[@class='style-scope ytcp-video-info']"
    HREF = 'href'
    UPLOADED = 'Uploading'
    ERROR_CONTAINER = '//*[@id="error-message"]'
    VIDEO_NOT_FOUND_ERROR = 'Could not find video_id'
    DONE_BUTTON = 'done-button'
    INPUT_FILE_VIDEO = "//input[@type='file']"
    
    MONITIZATION_TAG_ICON = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-monetization/ytpp-video-monetization-basics/div/div[1]/div/div/ytcp-video-metadata-monetization/ytcp-form-input-container/div[1]/div[2]/ytcp-video-monetization/div/div/div/ytcp-icon-button/tp-yt-iron-icon'
    MONITIZATION_TAG = '//*[@id="radio-on"]'
    MONITIZATION_TAG_BUT = '/html/body/ytcp-video-monetization-edit-dialog/tp-yt-paper-dialog/div/div/ytcp-button[2]/div'
    
    PRIVATE_TAG = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[1]'
    
    UNLISTED_TAG = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]'
    
    PUBLIC_TAG = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]'
    
    SECOND_EXTRA_CLICK = '//*[@id="checkbox-container"]'
    
    INPUT_FILE_THUMB = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[3]/ytcp-thumbnails-compact-editor/div[3]/ytcp-thumbnails-compact-editor-uploader'
    INPUT_FILE_THUMBNAIL = "//input[@type='file']"
    
    SWITCH_ACCOUNT = '//*[@id="avatar-btn"]'
    SWITCH_ACCOUNT2 = '/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[4]/a/tp-yt-paper-item'
    
    SWITCH_ACCOUNT3 = '/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[%d]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer/tp-yt-paper-icon-item'
    
    PUBLIC_BUTTON = '/html/body/ytcp-prechecks-warning-dialog/ytcp-dialog/tp-yt-paper-dialog/div[3]/div/ytcp-button[1]/div'
    

