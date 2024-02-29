flowFile = session.get()
if (flowFile != null) {
    // Get the 'rule_applied' attribute
    ruleApplied = flowFile.getAttribute('rule_applied')

    // Check if the rule has not been applied
    if (ruleApplied == 'false') {
        // Your rule processing logic goes here
        // For example, log a message and update the 'rule_applied' attribute
        log.info("Rule Processing: Rule not applied. Applying rule...")
        flowFile = session.putAttribute(flowFile, 'rule_applied', 'true')

        // Transfer the flow file to a success relationship
        session.transfer(flowFile, REL_SUCCESS)
    } else {
        // If the rule has already been applied, transfer the flow file to a different relationship
        log.info("Rule Processing: Rule already applied. Skipping...")
        session.transfer(flowFile, REL_ALREADY_APPLIED)
    }
}
