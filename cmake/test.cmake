add_custom_target("pytest"
    COMMENT "Running PyTest tests"
    # DEPENDS ${PROJECT_NAME}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
    COMMAND python -m pytest tests/
)
