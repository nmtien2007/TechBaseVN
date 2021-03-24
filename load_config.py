import os
import sys
import shutil

if __name__ == "__main__":
    print('START LOAD CONFIG SETTING')
    deploy_type = "dev_config"
    if len(sys.argv) >= 2:
        if sys.argv[1] in ["live_config", "dev_config"]:
            deploy_type = sys.argv[1]

    #prepare some constants
    CURRENT_DIR = os.getcwd()
    DEPLOY_CONFIG_DIR = os.path.join(CURRENT_DIR, "multi_configs")

    TARGET_CONFIG_FILE_DIR = os.path.join(CURRENT_DIR,  "TechBaseVN", "config.py")

    # update config file
    shutil.copy(os.path.join(DEPLOY_CONFIG_DIR, "%s.py" % deploy_type), TARGET_CONFIG_FILE_DIR)
    print("END LOAD CONFIG SETTING")
